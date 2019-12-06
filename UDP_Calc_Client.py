'''
Name: UDP_Calc_Client.py
Desc: An example UDP Calculator Client
Auth: Martin Georgiev
Date: 22/11/19
'''

import socket  # Imports socket library

SERVER_NAME = 'localhost'  # Specifies the server is local (127.0.0.1)
SERVER_PORT = 12345  # Specifies server port

# Opens the server socket (UDP)
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Client loop
while True:
    # Inputs type of operand
    operand = input('Please enter the type of operand: ')
    operatorA = input('Please enter operator A: ')  # Inputs operatorA
    operatorB = input('Please enter operator B: ')  # Inputs operatorB

    message = operand + " " + operatorA + " " + operatorB
    # Sends the encoded packets to the server
    CLIENT_SOCKET.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))   
    # Receives answer
    ANSWER_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(2048)

    print('Result: ' + (ANSWER_MESSAGE.decode()))  # Prints answer

# Closes the server socket
CLIENT_SOCKET.close()
