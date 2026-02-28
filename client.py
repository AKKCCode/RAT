import socket
import threading

TARGET = "127.0.0.1"

PORT = 777

PORT2 = 888

def listen():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((TARGET, PORT2))

        s.listen()

        conn, addr = s.accept()
        print(f"connected to {addr}")

        with conn:
            while True:
                msg = conn.recv(2048).decode()
                if not msg:
                    break
                print(msg)


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect(("127.0.0.1", 777))

        while True:
            msg = input("")

            s.sendall(msg.encode())

t = threading.Thread(target=listen)
t.start()
q = threading.Thread(target=main)
q.start()
