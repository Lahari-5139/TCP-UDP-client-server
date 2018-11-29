from socket import *
serverName = '172.16.92.176'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
data = raw_input('enter the numbers:')
clientSocket.sendto(data,('',12345))
newdata, serverAddress = clientSocket.recvfrom(2048)
print 'In sorted Order:',newdata
clientSocket.close()
