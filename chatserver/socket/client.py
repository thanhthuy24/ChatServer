import socket

HOST = '127.0.0.1'
SERVER_PORT = 51263
FORMAT = 'utf8'

def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        #waiting response
        client.recv(1024)

    msg = "end"
    client.sendall(msg.encode(FORMAT))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("CLIENT SIDE")

try:
    client.connect((HOST, SERVER_PORT))
    print("client address: ", client.getsockname())

    list = ["duchieuvn", "15", "nam"]

    msg = None
    while(msg != "x"):
        msg = input("Talk: ")
        # gửi lệnh đi
        client.sendall(msg.encode(FORMAT))
        msg = client.recv(1024).decode(FORMAT)
        print("Server response: ", msg)

        if (msg == "list"):
            # wait response
            client.recv(1024)
            sendList(client, list)


except:
    print("Error")

print("End")
client.close()