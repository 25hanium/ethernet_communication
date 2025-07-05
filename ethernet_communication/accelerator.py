import socket
import torch
import io
from PIL import Image
from torchvision import transforms
from .model import loadDefaultModel
from .ethernet import Ethernet

class Accelerator(Ethernet):
    def __init__(self, HOST, log=False, tag='', model=loadDefaultModel(), input_shape=(3, 224, 224)):  
        super().__init__(HOST, log, tag)
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
        while True:
            conn, addr = self.server_socket.accept()
            self.logger(f"Connected by {addr}")

            try:
                image_bytes = b''
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    image_bytes += data
                
                image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
                image = self.transform(image).unsqueeze(0).to(self.device)
                
                with torch.no_grad():
                    res = self.model(image)
            
                conn.sendall(res.cpu().numpy().tobytes())
                self.logger(f"Send evaluation result.")
            except Exception as e:
                self.logger(f"Error processing request: {e}")
            finally:
                conn.close()

    def __del__(self):
        if hasattr(self, 'server_socket'):
            self.server_socket.close()
            self.logger("Server socket closed.")