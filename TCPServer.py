from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "O Servidor esta pronto para uso"
while 1:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	modifiedMessage = message.upper()
	connectionSocket.send(modifiedMessage)
	connectionSocket.close()