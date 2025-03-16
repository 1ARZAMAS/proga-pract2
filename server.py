import socket

def server() -> None:
    HOST = '172.17.3.99'
    PORT = 6354

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    print(f"Server is listening on {HOST}:{PORT}...")

    conn, address = server_socket.accept()
    print("Connection from:", address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("From connected user:", data)

        response = "Машина выехала по адресу: " + data

        conn.send(response.encode())

    conn.close()
    print("Connection closed.")

if __name__ == '__main__':
    server()