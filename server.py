import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server_socket.bind(("0.0.0.0", 8081))

# Enable listening
server_socket.listen()

print("Server is listening at port 8081")

# Accept connection
connection_socket, address = server_socket.accept()

print("Connected with ", client_address)

# Send something to the client

message = "Hey there, thank you for connecting with me"

data = message.encode()

connection_socket.send(data)

# Hearing back from the client
client_message = connection_socket.recv(1024)

client_message.decode()

print(client_message)

# Time for some closure

connection_socket.close()
server_socket.close()
