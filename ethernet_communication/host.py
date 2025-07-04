import socket
import io
import numpy as np
from PIL import Image
from .ethernet import Ethernet

class Host(Ethernet):
    def __init__(self, HOST, log=False, tag=''):  
        super().__init__(HOST, log, tag)
        self.supportFormat = [(np.ndarray, self.numpy2byte)]

    def numpy2byte(self, img):
        img = Image.fromarray(img.astype('uint8'))
        with io.BytesIO() as output:
            img.save(output, format="PNG")
            image_bytes = output.getvalue()

        return image_bytes
        

    def __call__(self, img):
        for ty, encoder in self.supportFormat:
            if (type(img) is not ty):
                continue
            image_bytes = encoder(img)
            break
        else:
            print(f"Wrong input type. received {type(img)}.")
            return -1


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.HOST, self.PORT))
            self.logger(f"Connected to {self.HOST}:{self.PORT}")

            client.sendall(image_bytes)
            client.shutdown(socket.SHUT_WR) # Signal end of sending

            self.logger("Image sent. Waiting for evaluation result...")

            buffer = b''
            while True:
                data = client.recv(4096)
                if not data:
                    break
                buffer += data
            
            result = np.frombuffer(buffer, dtype=np.float32)
            self.logger(f"Received evaluation result: {result}")
            
            return result
