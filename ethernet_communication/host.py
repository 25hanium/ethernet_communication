import socket
import io
import numpy as np
from PIL import Image
from .ethernet import Ethernet

class Host(Ethernet):
    def __init__(self, HOST, log=False, tag='', logLevel=0):  
        super().__init__(HOST, log, tag, logLevel)
        self.supportFormat = [(np.ndarray, self.numpy2byte)]
        # Initialize client socket for persistent connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.logger(f"Connected to {self.HOST}:{self.PORT}")

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

        # Send image size first
        image_size = len(image_bytes)
        self.client_socket.sendall(image_size.to_bytes(4, 'big'))
        self.client_socket.sendall(image_bytes)

        self.logger("Image sent. Waiting for evaluation result...")

        # Receive result size first
        result_size_bytes = self.client_socket.recv(4)
        if not result_size_bytes:
            raise Exception("Did not receive result size.")
        result_size = int.from_bytes(result_size_bytes, 'big')

        buffer = b''
        bytes_received = 0
        while bytes_received < result_size:
            data = self.client_socket.recv(min(4096, result_size - bytes_received))
            if not data:
                break
            buffer += data
            bytes_received += len(data)
        
        if bytes_received != result_size:
            raise Exception(f"Incomplete result data received. Expected {result_size}, got {bytes_received}")
        
        self.logger("Evaluation result received.")

        return np.frombuffer(buffer, dtype=np.float32)

    def __del__(self):
        if hasattr(self, 'client_socket'):
            self.client_socket.close()
            self.logger("Client socket closed.")