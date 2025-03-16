import socket

def client() -> None:
    """
    Клиент
    """
    HOST = '217.71.129.139'
    PORT = 5399

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            message = input(" >> ")

            if message.lower().strip() == 'bye':
                print("Closing connection...")
                break

            client_socket.send(message.encode())

            data = client_socket.recv(1024).decode()
            if not data:
                print("Server closed the connection.")
                break

            print('Received from server:', data)

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and reachable.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == '__main__':
    client()