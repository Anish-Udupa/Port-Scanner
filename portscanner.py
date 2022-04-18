import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

host = input("Enter the host ip address: ")
port = int(input("Enter the host port number: "))

def port_scanner(host, port):
    if s.connect_ex((host, port)):
        print("Port {} is closed.".format(port))
    else:
        print("Port {} is open.".format(port))

port_scanner(host, port)
