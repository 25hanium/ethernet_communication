import socket
import os
from .ethernet import Ethernet

class Host(Ethernet):
  def __init__(self, HOST, log=False, tag=''):  
    super().__init__(HOST, log, tag)
    self.path = 'image.png'

  def __call__(self):
    if not os.path.exists(self.path):
        print("[RPI] Image file not found.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((self.HOST, self.PORT))
        self.logger(f"Connected to {self.HOST}:{self.PORT}")

        with open(self.path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                client.sendall(chunk)

        self.logger("File sent. Waiting for confirmation...")

        response = client.recv(1024)
        if response == b'SUCCESS':
            self.logger("Transmission successful.")
        else:
            self.logger("Transmission failed.")
