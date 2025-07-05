class Ethernet():
  def __init__(self, HOST, log=False, tag='', logLevel=0):  
    self.HOST, self.PORT = self.getHost(HOST)
    self.logEnable = log
    self.tag = ', '+tag
    self.logLevel = logLevel
    
  def getHost(self, ss):
    if (':' not in ss):
      raise Exception(f"Wrong host input. Expected 'x.x.x.x:xxxx'. But get {ss}")

    host, port = ss.split(':')
    return host, int(port)

  def logger(self, ss, level=0):
    if (not self.logEnable or self.logLevel > level):
      return
    print(f"#Ethernet{self.tag} : {ss}")
