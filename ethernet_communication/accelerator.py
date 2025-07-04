import socket
import torch
from .model import model
from .ethernet import Ethernet

class Accelerator(Ethernet):
  def __init__(self, HOST, log=False, tag=''):  
    super().__init__(HOST, log, tag, model=model, input_shape=(3, 224, 224))
    self.model = model
    self.input_shape = input_shape
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    self.path = ''
    # setup
    self.model.to(device)
    self.model.eval()

  def __call__(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((self.HOST, self.PORT))
        server.listen(1)
        self.logger(f"Listening on port {self.PORT}...")

        conn, addr = server.accept()
        self.logger(f"Connected by {addr}")

        with open(self.path, 'wb') as f:
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)

        self.logger(f"File saved as {self.path}")

        if (data.shape == self.input_shape)
        res = model(data)
      
        conn.sendall(res)
        self.logger(f"Send evaluation result.")
      
        conn.close()
