import ethernet_communication as ec

IP = '169.254.51.93:5000'

acc = ec.Accelerator(IP, True)
res = acc()
print(res)
