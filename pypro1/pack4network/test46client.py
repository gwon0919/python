from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 6666))
clientsock.send('안녕 방가워'.encode(encoding='utf_8', errors='strict'))
re_msg = clientsock.recv(1024).decode()
print('수신 자료 : ' + re_msg)
clientsock.close()
