from http import client
import socket

HOST = '127.0.0.1'
PORT = 8081

server = socket.socket()
server.bind((HOST, PORT))
print("[-->] Server Started")
print("[-->] Wating For Connection Of Client...")
server.listen(1)
client, client_addr = server.accept()
print(f'[-->] {client_addr} Client Connected To Server!')

while True:
    command = input('Enter Command: ')
    command = command.encode()
    client.send(command)
    print('[-->] Command Sent!')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")