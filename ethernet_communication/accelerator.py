import socket
from .ethernet import Ethernet

class Accelerator(Ethernet):
  def __init__(self, HOST, log=False, tag=''):  
    super().__init__(HOST, log, tag)
    self.path = ''

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

        # 여기에 CNN 가속기 삽입
      
        conn.sendall(b'SUCCESS')
        self.logger(f"Send evaluation result.")
      
        conn.close()
