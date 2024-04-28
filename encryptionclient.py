import socket
import random

def mod_exp(a, b, p):
    return pow(a, b, p)

def diffie_hellman(client_socket):
    p = 23
    g = 5
    private_key = random.randint(1, p - 1)
    public_key = mod_exp(g, private_key, p)

    client_socket.send(str(public_key).encode())
    server_public_key = int(client_socket.recv(1024).decode())

    shared_secret = mod_exp(server_public_key, private_key, p)
    return shared_secret

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))

shared_secret = diffie_hellman(client_socket)
print("Общий секрет:", shared_secret)

client_socket.close()
