import ethernet_communication as ec
import numpy as np
 
IP = '192.168.137.10:7'
R, C, CH = 32, 32, 3
i_type = np.uint8
i_byte = 1
input_size = R*C*CH
o_type = np.float32
o_byte = 4
output_size = 128

acc = ec.Accelerator(
    HOST=IP, 
    log=True, 
    logLevel=1,
    i_type=i_type,
    i_byte=i_byte,
    input_size=input_size,
    o_type=o_type,
    o_byte=o_byte,
    output_size=output_size
)

log = acc()
print(log) # if error occered, print '-1'
