import ethernet_communication as ec
import numpy as np
 
IP = '192.168.137.1:5000'
acc = ec.Accelerator(IP, True, logLevel=1)

# Start Communication
log = acc()
print(log) # if error occered, print '-1'
