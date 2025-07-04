import ethernet_communication as ec
import numpy as np

IP = '127.0.0.1:5000'

host = ec.Host(IP, True)

random_image = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
res = host(random_image)
print(res)