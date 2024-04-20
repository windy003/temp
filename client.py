import socket
import threading

def receive_message(socket):
    while True:
        try:
            data = socket.recv(1024)
            if not data:
                break
            print(f"来自服务器: {data.decode()}")
        except:
            print("服务器连接已断开。")
            break

def client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("已连接到服务器，可以发送消息。")

    threading.Thread(target=receive_message, args=(client_socket,)).start()

    try:
        while True:
            message = input("请输入消息: ")
            client_socket.sendall(message.encode())
            if message.lower() == 'quit':
                break
    finally:
        client_socket.close()
        print("连接已关闭。")

if __name__ == '__main__':
    client()
