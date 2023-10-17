# 단순 클라이언트 
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 8888))
clientsock.send('안녕 방가워'. encode(encoding='utf-8', errors='strict'))
clientsock.close()

