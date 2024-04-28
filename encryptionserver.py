import socket
import random

def mod_exp(a, b, p):
    return pow(a, b, p)

def diffie_hellman(server_socket):
    p = 23
    g = 5
    private_key = random.randint(1, p - 1)
    public_key = mod_exp(g, private_key, p)

    client_public_key = int(server_socket.recv(1024).decode())
    server_socket.send(str(public_key).encode())

    shared_secret = mod_exp(client_public_key, private_key, p)
    return shared_secret

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(1)

print("Сервер запущен. Ожидание подключений...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Принято соединение от {client_address}")

    shared_secret = diffie_hellman(client_socket)
    print("Общий секрет:", shared_secret)

    client_socket.close()
