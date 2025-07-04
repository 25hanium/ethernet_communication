import ethernet_communication as ec

IP = '127.0.0.1:5000'

acc = ec.Accelerator(IP, True)
res = acc()
print(res)
