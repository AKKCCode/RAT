import getpass
import socket
import time
import os

hostname = socket.gethostname()
whoami = getpass.getuser()

CMD_PATH = r"C:\Apache24\htdocs\cmd.txt"
ACT_PATH = r"C:\Apache24\htdocs\cmda.txt"

while True:
    rcommand = input(f"{hostname}, {whoami} > ")
    if not rcommand:
        continue

    # write command
    with open(CMD_PATH, "w") as f:
        f.write(rcommand + "\n")
        f.flush()
        os.fsync(f.fileno())   # force write to disk

    # activate
    with open(ACT_PATH, "w") as s:
        s.write("3")
        s.flush()
        os.fsync(s.fileno())

    # give reader time to react (optional, shorter)
    time.sleep(0.5)

    # reset
    with open(ACT_PATH, "w") as s:
        s.write("0")
        s.flush()
        os.fsync(s.fileno())
