import socket

def client() -> None:
    """
    Эхо
    """
    HOST = '217.71.129.139'
    PORT = 4445
    client_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM) 
    
    try:
        client_socket.connect((HOST, PORT))
        
        while True:
            message = input(" >> ")

            if message.lower().strip() == 'bye':
                break

        client_socket.send(message.encode())
        data = client.socket.recv(1024) .decode()

        print ('Received from server: ' + data)

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and reachable.")
    finally:
        client_socket.close()

if __name__ == '__main__':
    client()