# Network
# Socket : 네트워크를 위한 통신 채널을 지원
import socket

print(socket.getservbyname('http','tcp'))   # 80
print(socket.getservbyname('https','tcp'))  # 443
print(socket.getservbyname('telnet','tcp')) # 23
print(socket.getservbyname('ftp','tcp'))
print(socket.getservbyname('smtp','tcp'))
print(socket.getservbyname('pop3','tcp'))

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 223.130.195.95     223.130.200.104 하나의 도메인의 여러 개의 ip addr 

