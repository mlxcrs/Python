from socket import *
serverName = "10.71.21.12"
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Insira uma mensagem com letras minusculas: ')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()