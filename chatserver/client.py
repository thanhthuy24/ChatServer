import socket

HOST = '127.0.0.1'
SERVER_PORT = 51263
FORMAT = 'utf8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT SIDE")

try:
    client.connect((HOST, SERVER_PORT))
    print("client address: ", client.getsockname())

    msg = None
    while(msg != "x"):
        msg = input("Talk: ")
        # gửi lệnh đi
        client.sendall(msg.encode(FORMAT))
        msg = client.recv(1024).decode(FORMAT)
        print("Server response: ", msg)

except:
    print("Error")

print("End")
client.close()