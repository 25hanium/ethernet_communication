import socket
import torch
import numpy as np
import io
from PIL import Image
from time import time
from torchvision import transforms
from .model import loadDefaultModel
from .ethernet import Ethernet

class Accelerator(Ethernet):
    def __init__(self, HOST, log=False, tag='', logLevel=0, model=loadDefaultModel(), i_type=int, i_byte=4, input_size=3*224*224, o_type=float, o_byte=4,  output_size=128):  
        super().__init__(HOST, log, tag, logLevel)
        self.model = model
        self.i_type = i_type
        self.i_byte = i_byte
        self.input_size = input_size
        self.input_byte_size = i_byte*input_size
        self.o_byte = o_byte
        self.o_type = o_type
        self.output_size = output_size
        self.output_byte_size = o_byte*input_size
        # model
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # setup
        self.model.to(self.device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        # Initialize server socket for persistent listening
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(1)
        self.logger(f"Listening on port {self.PORT}...")
    
    def __call__(self):
        while True: 
            conn, addr = self.server_socket.accept()
            self.logger(f"Connected by {addr}")
            
            while True: 
                try:    
                    image_bytes = b''
                    while len(image_bytes) < self.input_byte_size:
                        self.logger(f"image_bytes len: {len(image_bytes)}")
                        packet = conn.recv(self.input_byte_size - len(image_bytes))
                        if not packet:
                            self.logger(f"Client {addr} disconnected.")
                            break # Exit inner loop if client disconnects
                        image_bytes += packet
                    
                    if not image_bytes: # If no bytes received, client disconnected
                        break

                    # Convert 1D byte array to numpy array and reshape to image dimensions
                    image_np = np.frombuffer(image_bytes, dtype=self.i_type)
                    # Assuming input_size is H*W*C for a flattened image
                    # Reshape to (H, W, C) for PIL.Image.fromarray
                    # Assuming 3 channels (RGB) and square image for simplicity, adjust if needed
                    side_length = int(np.sqrt(self.input_size / 3)) 
                    image = Image.fromarray(image_np.reshape((side_length, side_length, 3)))
                    
                    self.logger("Run model")
                    s = time()
                    image = self.transform(image).unsqueeze(0).to(self.device)
                    with torch.no_grad():
                        res = self.model(image)
                    e = time()

                    res = res.cpu().numpy()
                    result_bytes = res.astype(self.o_type).tobytes()
                    conn.sendall(result_bytes) # Then send the actual result
                    self.logger(f"Send evaluation result to {addr}.")

                    self.logger(f'sum(res): {np.sum(res):.3f} ({e-s:.3f})', 1)
                except Exception as e:
                    self.logger(f"Error processing request from {addr}: {e}")
                    break  

            conn.close()
            return -1

    def __del__(self):
        if hasattr(self, 'server_socket'):
            self.server_socket.close()
            self.logger("Server socket closed.")
