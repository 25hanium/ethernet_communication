import socket
import io
import numpy as np
from PIL import Image
from .ethernet import Ethernet

class Host(Ethernet):
    def __init__(self, HOST, log=False, tag='', logLevel=0, i_type=int, i_byte=4, input_size=3*224*224, o_type=float, o_byte=4,  output_size=128):  
        super().__init__(HOST, log, tag, logLevel)
        self.i_type = i_type
        self.i_byte = i_byte
        self.input_size = input_size
        self.input_byte_size = i_byte*input_size
        self.o_byte = o_byte
        self.o_type = o_type
        self.output_size = output_size
        self.output_byte_size = o_byte*output_size
        # Initialize client socket for persistent connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.logger(f"Connected to {self.HOST}:{self.PORT}")
    
    def __call__(self, img):
        if not isinstance(img, np.ndarray):
            print(f"Wrong input type. received {type(img)}. Expected numpy.ndarray.")
            return -1
        
        image_bytes = img.astype(self.i_type).tobytes()
        self.client_socket.sendall(image_bytes)

        self.logger("Image sent. Waiting for evaluation result...")

        buffer = self.client_socket.recv(self.output_byte_size)
        
        self.logger("Evaluation result received.")

        return np.frombuffer(buffer, dtype=self.o_type)

    def __del__(self):
        if hasattr(self, 'client_socket'):
            self.client_socket.close()
            self.logger("Client socket closed.")
