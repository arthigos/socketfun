import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to connect
client_socket.connect(("127.0.0.1", 8081))

print("Client has connected to the server")

# Getting data from server using the socket

data = client_socket.recv(1024)

message = data.decode()

print(message)

# Sending data to the server

client_data = "Hi there, client over here. Thank you for letting me connect =]"

client_data = client_data.encode()

client_socket.send(client_data)

# Time for some closure

client_socket.close()
