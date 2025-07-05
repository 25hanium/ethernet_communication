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
    def __init__(self, HOST, log=False, tag='', logLevel=0, model=loadDefaultModel(), input_shape=(3, 224, 224)):  
        super().__init__(HOST, log, tag, logLevel)
        # model
        self.model = model
        self.input_shape = input_shape
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
        while True: # Loop to accept new client connections
            conn, addr = self.server_socket.accept()
            self.logger(f"Connected by {addr}")
            
            # Inner loop to handle multiple requests from the same client
            while True: 
                try:
                    # Receive image size first
                    image_size_bytes = conn.recv(4)
                    if not image_size_bytes: # Client disconnected
                        self.logger(f"Client {addr} disconnected.")
                        break # Break from inner loop, go back to accept new client
                    image_size = int.from_bytes(image_size_bytes, 'big')

                    image_bytes = b''
                    bytes_received = 0
                    while bytes_received < image_size:
                        data = conn.recv(min(4096, image_size - bytes_received))
                        if not data: # Client disconnected during data transfer
                            self.logger(f"Client {addr} disconnected during data transfer.")
                            break # Break from inner loop
                        image_bytes += data
                        bytes_received += len(data)
                    
                    if bytes_received != image_size:
                        raise Exception(f"Incomplete image data received. Expected {image_size}, got {bytes_received}")
                    
                    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

                    s = time()
                    image = self.transform(image).unsqueeze(0).to(self.device)
                    with torch.no_grad():
                        res = self.model(image)
                    e = time()

                    res = res.cpu().numpy()
                    result_bytes = res.tobytes()
                    result_size = len(result_bytes)
                    conn.sendall(result_size.to_bytes(4, 'big')) # Send result size first
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