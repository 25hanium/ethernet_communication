import ethernet_communication as ec
import numpy as np
from time import time

IP = '192.168.137.1:7'
i_type = int
i_byte = 4
input_size = 3*224*224
o_type = float
o_byte = 4
output_size = 128

host = ec.Host(IP, True,
    i_type=i_type,
    i_byte=i_byte,
    input_size=input_size,
    o_type=o_type,
    o_byte=o_byte,
    output_size=output_size)

N = 100
delay = []
s = time()
for i in range(N):
    # Communication
    random_image = np.ones((224, 224, 3), dtype=np.uint8)
    res = host(random_image)
    
    # log
    delay.append(time()-s)
    s = time()
    print(f"Loop {i} : sum(res) {np.sum(res):.3f} ({delay[-1]:.3f}s)")

# Result
print(f"\n※ Communication Result ※\n    fps: {1/np.average(delay)}Hz (sampling: {N})")
