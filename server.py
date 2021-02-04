import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind = (("0.0.0.0", 8081))
server_socket.listen()
print("Server is listening...")
connection_socket, address = server_socket.accept()
print("Client connected")
