from socket import *
serverName = '172.16.144.239'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,12345))
numbers = raw_input('input numbers')
clientSocket.send(numbers)
modifiednumbers = clientSocket.recv(1024)
print 'sorted order:', modifiednumbers
clientSocket.close()
