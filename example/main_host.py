import ethernet_communication as ec
import numpy as np
from time import time

IP = '192.168.137.10:7'
R, C, CH = 32, 32, 3
i_type = np.uint8
i_byte = 1
input_size = R*C*CH
o_type = np.float32
o_byte = 4
output_size = 128

host = ec.Host(IP, True,
    i_type=i_type,
    i_byte=i_byte,
    input_size=input_size,
    o_type=o_type,
    o_byte=o_byte,
    output_size=output_size,
    logLevel=1)

N = 1000
delay = []
s = time()
getAnswer = lambda img : sum([np.sum(img)+i for i in range(output_size)]) 

print('############ Start testbench')
for i in range(N):
    random_image = (np.ones((R, C, CH))*10).astype(i_type)
    random_image[0, 0, 0] += i
    res = host(random_image)
    
    answer = getAnswer(random_image)

    integrity = True if (answer == sum(res)) else False
    
    delay.append(time()-s)
    s = time()
    print(f"Loop {i+1} integrity : {integrity} ")

# Result
print(f"\n※ Communication Result ※\n    fps: {1/np.average(delay)}Hz (sampling: {N})")