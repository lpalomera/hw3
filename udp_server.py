#Anthony Palomera
#CS176A
#Hw3

#Outline:
#Outline written by Atefeh Mohseni
#https://piazza.com/redirect/s3?bucket=uploads&prefix=paste%2Fk18ujakbwvq4ix%2F6499e107e636a7c0a1ba0ba9c6c85308e2bdd18704cc72dfd7c69b539c6db6ae%2Fudp_server.py

#Imports
from socket import *
from sys import argv
 
#Inputs
PORT = int(argv[1])
SERVER = "127.0.0.1"
ZONE = 'utf-8'
SIZE = 128
 
#Create socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
 
#Bind socket
serverSocket.bind((SERVER, PORT))
 
connected = 1
 
while connected:
    #Receive data from client
    message, clientAddress = serverSocket.recvfrom(SIZE)
    
    #Make sure there are nothing but numbers
    if(message.decode(ZONE).isnumeric()):
        sum = 0
        for char in message.decode(ZONE):
            sum += int(char)

        #Send response until there is a single digit
        while(sum > 0):
            responseMessage = str(sum)
            serverSocket.sendto(responseMessage.encode(ZONE), clientAddress)
            if(sum < 10):
                break
            sum = 0 #Reset sum
            for char in responseMessage:
                sum += int(char)
    #In the case there are non-numbers in the string
    else:
        responseMessage = "Sorry, cannot compute!"
        serverSocket.sendto(responseMessage.encode(ZONE), clientAddress)
