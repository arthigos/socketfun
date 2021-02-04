import socket

def send_text(sending_socket, text):
    text = text + "\n"  # test with append EOT (\4)
    data = text.encode()
    sending_socket.send(data)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server_socket.bind(("0.0.0.0", 8081))

# Enable listening
server_socket.listen()

print("Server is listening at port 8081")

# Accept connection
connection_socket, client_address = server_socket.accept()

print("Connected with ", client_address)

# Send something to the client

message = "Hey there, server here. Thank you for connecting with me"

send_text(connection_socket, message)

# Hearing back from the client
client_message = connection_socket.recv(1024)

client_message.decode()

print(client_message)

# Time for some closure

connection_socket.close()
server_socket.close()
