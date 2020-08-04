from socket import *
from time import sleep
from os import path
from _pickle import loads
def fu(a=SOCK_STREAM):
   
   port = 9999
   ip = '0.0.0.0'
   global classs
   classs = socket(AF_INET,a)
   classs.bind((ip,port))
   classs.listen(5)
   #while True:
    #  global fd
   fd,add = classs.accept()
   sleep(0.1)
   fd.send(b'ok 2-00')
   d = fd.recv(1024)
   name = loads(d)
   open_txt(name)
   sleep(0.1)
   info = f'{name} |{str(path.getsize(name))}'
   fd.send(bytes(info,encoding="utf-8"))
   sleep(0.1)
   data = fd.recv(1024)
   if str(data,encoding='utf-8') == 'ok':
     sleep(0.1) 
     fd.send(da)
   else:
      print('not ok')
     
   fd.close
   print('ok')
def open_txt(name):
   print('open txt')
   with open(name,'rb') as ff:
        global da    
        da = ff.read() 

if __name__ == '__main__':
 fu()
