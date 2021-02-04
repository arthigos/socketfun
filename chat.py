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

def send_text(sending_socket, text):
    text = text + "\n"  # test with append EOT (\4)
    data = text.encode()
    sending_socket.send(data)

# Choose between client or server
option = input("Choose (client or server): ")

if option == 'client':
    print("Send 'later' to end the connection")  
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Ask for desired server IP
    ip = input("What is the server's ip? Press enter for default. Default is 127.0.0.1 ") or "127.0.0.1"
    username = input("Provide a username: ")
    #Try to connect
    client_socket.connect((ip, 8081))
    print(username + " has connected to the server")

    # 'Chat' loop
    while True:
        client_message = input("Type a message to send: ")
        data = client_message.encode()
        client_socket.send(data)

        message = next(get_text(client_socket))
        print(username + " sent: " + client_message)
        #for message in get_text(client_socket):
        #    print(username + " received: " + client_message)
    # Time for some closure
    client_socket.close()
    
elif option == 'server':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket
    server_socket.bind(("0.0.0.0", 8081))
    # Enable listening
    server_socket.listen()
    # Accept connection
    connection_socket, client_address = server_socket.accept()
    print("Connected with someone") # improve with client_address
    # Send something to the client
    message = "Hey there, server here. Thank you for connecting with me"
    send_text(connection_socket, message)

    #Chat loop
    while True:
        client_data = connection_socket.recv(1024)
        client_message = client_data.decode()
        print("Server received: " + message) # add sender info
        #acknowledge
        ack = "message received!"
        send_text(connection_socket, ack)

        #define a escape route
        if client_message == str('later'):
            send_text(connection_socket, "It has been good serving you. Until we meet again")
            connection_socket.close()
            server_socket.close()

else:
    print("Start over")
    exit()
