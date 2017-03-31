from socket import *
serverName = "moclet04l07"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = raw_input('Insira uma mensagem com letras minusculas: ')
clientSocket.send(message)
modifiedMessage = clientSocket.recv(1024)
print 'From Server: ', modifiedMessage
clientSocket.close()