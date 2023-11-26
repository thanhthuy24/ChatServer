# import socket
#
# #192.168.2.7
# HOST = "127.0.0.1"
# SERVER_PORT = 51263
# FORMAT = "utf8"
#
# def recvList(socket):
#     list = []
#     item = conn.recv(1024).decode(FORMAT)
#     while (item != "end"):
#
#         list.append(item)
#         #response
#         conn.sendall(item.encode(FORMAT))
#         item = conn.recv(1024).decode(FORMAT)
#
#     return list
#
# #socket.AF_INET -- dùng để thiết lập ipv4
# #socket.SOCK_STREAM -- dùng để thiết lập TCP
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #bind.. -- lắng nghe địa chỉ address và port
# s.bind((HOST, SERVER_PORT))
# s.listen()
#
# print("SERVER SIDE")
# print("server: ", HOST, SERVER_PORT)
# print("Waiting for client")
#
# try:
#     conn, addr = s.accept()
#
#     print("client address: ", addr)
#     print("conn: ", conn.getsockname())
#
#     msg = None
#     while(msg != "x"):
#         msg = conn.recv(1024).decode(FORMAT)
#         print("client ", addr, "says ", msg)
#         msg = input("Server response: ")
#         conn.sendall(msg.encode(FORMAT))
#
#         if (msg == "list"):
#             conn.sendall(msg.encode(FORMAT))
#             list = recvList(conn)
#
#             print("received: ")
#             print(list)
#
# except:
#     print("Error")
#
# print("End")
# s.close()
#
#
import socket
import threading

import rsa

HOST = "127.0.0.1"
PORT = 9999
SIZE = 1024

public_key, private_key = rsa.newkeys(SIZE)
public_partner = None



choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(SIZE))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(SIZE))
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()


def sending_messages(c):
    while True:
        message = input()
        c.send(rsa.encrypt(message.encode(), public_partner))
        print("You: " + message)

def receiving_messages(c):
    while True:
        print("Partner: " + rsa.decrypt(c.recv(SIZE), private_key).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
