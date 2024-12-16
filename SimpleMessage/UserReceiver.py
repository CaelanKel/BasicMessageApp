import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(("IP your sending too (REPLACE)", 5555)) # listen on that ip with that port port must be same as server
client.listen(1)
running = True
while running:
    server,addr = client.accept()
    message = server.recv(1024).decode()
    print(message)
    break
