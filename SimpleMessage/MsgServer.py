import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",4444))

server.listen(1)
running = True
while running:  #accept a connection receive and decode the message while finding the ip from the message
    print("Server UP")
    client, addr = server.accept()
    print(f"Connecting to : client:{client}, address: {addr}")
    message = (client.recv(1024).decode())
    OutIP = ""
    IncomingIP = []
    for i in range(0,len(message)):
        if message[i] == "*":
            break
        else:
       
            IncomingIP.append(message[i])
    #strips message string for the ip address and adds it to OutIP
    for char in IncomingIP:
        OutIP += char
    OutIP.strip()
    client.send("Success".encode())
    print(f"Message: {message} IP ADDRESS: {OutIP}")
    running = False #breaks loop so we can connect to the recipient
server_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_client.connect((OutIP,5555))
server_client.send(message.encode())
print(f"Message sent to: {OutIP}")



    



        

    

    
    
    

    
    
    







