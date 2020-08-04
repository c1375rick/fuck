from socket import *
from time import sleep
from re import findall
from _pickle import dumps

def open_write(data,rd):
    with open(rd[0],'wb') as ff:
         ff.write(data) 
    print('ok')
def fu(a=SOCK_STREAM):
   port = 9999
   ip = '192.168.1.?'
   global classs
   classs = socket(AF_INET,a)
   classs.connect((ip,port))
   d = classs.recv(1024)
   name = input(str(d,encoding='utf-8')+'>>')
   sleep(0.1)
   classs.send(dumps(name)) 
   data = classs.recv(1024)
   rd = findall('.* |\d+',str(data,encoding='utf-8'))
   print(str(data,encoding='utf-8'))
   print(rd)
   classs.send(bytes('ok',encoding='utf-8'))
   data = classs.recv(int(rd[1]))
   classs.close()
   open_write(data,rd)
   
if __name__ == '__main__':
   fu()
