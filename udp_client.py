#Anthony Palomera
#CS176A 
#Hw3
#Outline:
#Outline written by Atefeh Mohseni
#https://piazza.com/redirect/s3?bucket=uploads&prefix=paste%2Fk18ujakbwvq4ix%2F8878c81398fe3ce4b23799dd8198239ffafc31389ea9d77a5d05fe66e3923b15%2Fudp_client.py

#Imports
from socket import *
from sys import argv
 
#Inputs
PORT = int(argv[2])
HOST = argv[1]
ZONE = 'utf-8'
SIZE = 128

#Create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Enter string: ", end="")
message = input()

#Send input to server
clientSocket.sendto(message.encode(ZONE), (HOST, PORT))

#Get and print responses
recvMessage, serverAddress = clientSocket.recvfrom(SIZE)
while(recvMessage):
    print("From server: " + recvMessage.decode(ZONE))
    
    #Make sure there are nothing but numbers
    if(recvMessage.decode(ZONE).isnumeric() == False):
        break

    #Send response until there is a single digit
    if(int(recvMessage.decode(ZONE)) < 10 ):
        break

    recvMessage, serverAddress = clientSocket.recvfrom(SIZE)

#Close socket
clientSocket.close()
