#Anthony Palomera
#CS176A 
#Hw3

#Outline:
#Outline by Atefeh Mohseni
#https://piazza.com/redirect/s3?bucket=uploads&prefix=paste%2Fk18ujakbwvq4ix%2F9ef915795c52f173ca7a26f72374677b134855f6840ff13bb576ff6ab61cac86%2Ftcp_server.py

#Imports
from socket import *
from sys import argv
import time

#Inputs
PORT = int(argv[1])
SERVER = "127.0.0.1"   #127.0.0.53
ZONE = 'utf-8'
SIZE = 128

#Create socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind the socket+port
serverSocket.bind((SERVER, PORT))

connected = 1
while connected:
    #Constantly listen to client
    serverSocket.listen()

    #Get connection req
    conn, addr = serverSocket.accept()
    with conn:

        #Receive data from client
        message = conn.recv(SIZE).decode(ZONE)

        #Make sure there are nothing but numbers
        if(message.isnumeric()):
            sum = 0
            for char in message:
                sum += int(char)
            
            #Send response until there is a single digit
            while(sum > 0):
                responseMessage = str(sum)
                conn.sendall(responseMessage.encode(ZONE))
                time.sleep(.1)
                
                if(sum < 10):
                    break
                sum = 0 #Reset sum
                for char in responseMessage:
                    sum += int(char)

        #In the case there are non-numbers in the string
        else:
            responseMessage = "Sorry, cannot compute!"
            conn.sendall(responseMessage.encode(ZONE))

    #Close connection
    conn.close()
