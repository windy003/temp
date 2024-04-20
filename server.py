import socket
import threading

clients = []

def broadcast_message(message):
    for client in clients:
        client.sendall(message.encode())

def handle_client(conn, addr):
    print(f"来自{addr}的连接已建立。")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"收到来自{addr}的消息: {message}")
            broadcast_message(f"{addr} 说: {message}")
    finally:
        conn.close()
        clients.remove(conn)
        print(f"与{addr}的连接已关闭。")

def server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print("服务器启动，等待连接...")

    threading.Thread(target=input_loop).start()

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def input_loop():
    while True:
        message = input("服务器输入消息: ")
        broadcast_message("服务器: " + message)

if __name__ == '__main__':
    server()
