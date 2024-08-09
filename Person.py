import socket
def send_message(server_ip='127.0.0.1', server_port=12345, message="Hello World!!1"):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")
        client_socket.sendall(message.encode('utf-8'))
        print(f"Send Message: {message}")
        client_socket.close()
        print("Connecton closed")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    send_message()

input()