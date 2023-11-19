import socket

#192.168.2.7
HOST = "127.0.0.1"
SERVER_PORT = 51263
FORMAT = "utf8"

#socket.AF_INET -- dùng để thiết lập ipv4
#socket.SOCK_STREAM -- dùng để thiết lập TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind.. -- lắng nghe địa chỉ address và port
s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server: ", HOST, SERVER_PORT)
print("Waiting for client")

try:
    conn, addr = s.accept()

    print("client address: ", addr)
    print("conn: ", conn.getsockname())

    msg = None
    while(msg != "x"):
        msg = conn.recv(1024).decode(FORMAT)
        print("client ", addr, "says ", msg)
        msg = input("Server response: ")
        conn.sendall(msg.encode(FORMAT))

except:
    print("Error")

print("End")
s.close()


