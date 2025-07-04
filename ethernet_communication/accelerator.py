import socket
import torch
import io
from PIL import Image
from torchvision import transforms
from .model import model
from .ethernet import Ethernet

class Accelerator(Ethernet):
  def __init__(self, HOST, log=False, tag='', model=model(), input_shape=(3, 224, 224)):  
    super().__init__(HOST, log, tag)
    self.model = model
    self.input_shape = input_shape
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    self.path = 'image.png'
    # setup
    self.model.to(self.device)
    self.model.eval()
    self.transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

  def __call__(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((self.HOST, self.PORT))
        server.listen(1)
        self.logger(f"Listening on port {self.PORT}...")

        conn, addr = server.accept()
        self.logger(f"Connected by {addr}")

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
      
        conn.close()
        return 0
