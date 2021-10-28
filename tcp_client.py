#Anthony Palomera
#CS176A
#Hw3

#Outline:
#Outline written by Atefeh Mohseni
#https://piazza.com/redirect/s3?bucket=uploads&prefix=paste%2Fk18ujakbwvq4ix%2F4e14212ff4f783228c6fb2dcf8bef8837e66120b127d55cc18dae7900ab02b9a%2Ftcp_client.py
 
#Imports:
from socket import *
from sys import argv
 
#Inputs:
HOST = argv[1]
PORT = int(argv[2])
ZONE = 'utf-8'
SIZE = 128
 
#Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
 
#Connection req
clientSocket.connect((HOST, PORT))
 
print("Enter string: ", end="")
message = input()
 
#Send data to server
clientSocket.sendall(message.encode(ZONE))
 
#Receive response from server
data = clientSocket.recv(SIZE).decode(ZONE)
 
while(data):
    print("From server: " + data)
    #Make sure there are nothing but numbers
    if(data.isnumeric() == False):
        break
   
    #Send response until there is a single digit
    if(int(data) < 10):
        break
   
    #Receive updated data
    data = clientSocket.recv(SIZE).decode(ZONE)
 
#Close
clientSocket.close()
