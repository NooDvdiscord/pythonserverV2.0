import socket
import logging
import csv
from datetime import datetime
def start_server(host='0.0.0.0', port=12345):
    csv_file='connections.csv'
    logging.basicConfig(filename='server.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(massage)s')
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info(f'Start server on {host}:{port}. . .')

    try:
        file_empty = False
        try:
            with open(csv_file, 'r') as file:
                file_empty = (file.read(1) == '')
        except FileExistsError:
            file_empty = True
        
        with open(csv_file, 'a', newline= '') as file:
            writer = csv.writer(file)
            if file_empty:
                writer.writerow(['Timestamp', 'Clien IP', 'Client Port', 'Message'])
    except IOError as e:
        logging.error(f"Failed to write header to CSV file: {e}")
        return
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logging.info("Server is listening for connections. . .")

    while True:
        try:
            client_socket, address = server_socket.accept()
            logging.info(f"Connection from {address}")
            data = client_socket.recv(1024).decode('utf-8')
            logging.debug(f"Received raw data: {data}")
            if data:
                logging.info(f"Received dat: ")
                log_connection_csv(address, data, csv_file)
            else:
                logging.info("No data received.")
            client_socket.close()
        except Exception as e:
            logging.error(f"An error occurred: {e}")

def log_connection_csv(address, data, csv_file):
    try:
        timestamp = datetime.now().strftime('%Y-%M-%d %H:%M:%S')
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, address[0], address[1], data])
        logging.info(f"Logged data to CSV: {timestamp}, {address[0]}, {address[1]}, {data}")
    except IOError as e:
        logging.error(f"Failed to write to CSV file: {e}")

if __name__ == "__main__":
    start_server()

input()