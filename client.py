import socket

def get_text(receiving_socket):
    buffer = ""
    socket_open = True
    while socket_open:
      data = receiving_socket.recv(1024)
      if not data:
          socket_open = False
      buffer = buffer + data.decode()
      eot_pos = buffer.find("\n")

      while eot_pos > -1:
          message = buffer[:eot_pos]
          buffer = buffer[eot_pos + 1:]
          yield message
          eot_pos = buffer.find("\n")

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to connect
client_socket.connect(("127.0.0.1", 8081))

print("Client has connected to the server")

# Getting data from server using the client socket

#data = client_socket.recv(1024)

#message = data.decode()

#for message in get_text(client_socket):
message = next(get_text(client_socket))
print(message)

# Sending data to the server

client_data = "Hi there, client over here. Thank you for letting me connect =]"

client_data = client_data.encode()

client_socket.send(client_data)

# Time for some closure

client_socket.close()
