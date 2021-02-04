import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server_socket.bind = (("0.0.0.0", 8081))

# Enable listening
server_socket.listen()

print("Server is listening...")

# Accept connection
connection_socket, address = server_socket.accept()

print("Client connected")

# Send something to the client

message = "Hey there, thank you for connecting with me"

data = message.encode()

connection_socket.send(data)

# Time for some closure

connection_socket.close()
server_socket.close()
