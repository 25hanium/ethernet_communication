import ethernet_communication as ec
import numpy as np
from time import time

IP = '192.168.137.1:5000'
host = ec.Host(IP, True)

N = 100
delay = []
s = time()
for _ in range(N):
    random_image = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
    _ = host(random_image)
    delay.append(time()-s)
    s = time()
    
print(f"fps: {1/np.average(delay)}Hz (sampling: {N})")
