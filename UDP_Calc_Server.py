'''
Name: UDP_Calc_Server.py
Desc: An example UDP Calculator Server
Auth: Martin Georgiev
Date: 22/11/19
'''

import socket  # Imports socket library

SERVER_PORT = 12345  # Specifies the server's port

# Opens the server socket type (UDP)
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binds server to the specified port and localhost
SERVER_SOCKET.bind(('', SERVER_PORT))

# Server loop
while True:
    print('Server is up and running!')  # Message indicating the server is on

    # Receive incoming messages from the client address
    INCOMING_MESSAGE, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)

    # Prints incoming message
    message = INCOMING_MESSAGE.decode()
    print('Incoming Message: ', message)

    # Splits message into different variables
    operand, operatorA, operatorB = message.split()

    # Checks type of operand
    if operand == '+':
        result = int(operatorA) + int(operatorB)

    elif operand == '-':
        result = int(operatorA) - int(operatorB)

    elif operand == '*':
        result = int(operatorA) * int(operatorB)

    elif operand == '/':
        result = int(operatorA) / int(operatorB)

    ANSWER_MESSAGE = result

    # Sends encoded answer to the client
    SERVER_SOCKET.sendto(str(ANSWER_MESSAGE).encode(), CLIENT_ADDRESS)

# Closes server socket
SERVER_SOCKET.close()
