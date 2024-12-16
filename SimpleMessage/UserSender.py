import socket

ip= input("User IP: ")
message = input("Input message: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",4444))
10.
compMessage = ip + "*" + message
client.send(compMessage.encode())
input(" press any key to continue (wait 3 seconds)")
serverResponse = client.recv(1024).decode()
print(serverResponse)
if serverResponse == "Success":
    print("Success message sent.")
else:
    print("Message failed to send")


    




    


    