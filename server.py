import socket

HOST = '0.0.0.0'
PORT = 228

def server() -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    
    client, addr = s.accept()
    
    while True:
        command = str(input('Input command >> '))
        client.send(command.encode())
        
        if command.lower() == 'exit':
            break
        
        result = client.recv(1024).decode()
        print(result)
    
    client.close()
    s.close()

if __name__ == '__main__':
    server()