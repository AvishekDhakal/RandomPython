import socket 
import threading
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = "utf-8"
key = b"YELLOW SUBMARINE"


server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_soc.bind((SERVER,PORT))

def handle(conn,addr):
    print(f"Server is starting on {SERVER}:{PORT}")
    connected = True
    while connected:
        # msg_length_b = conn.recv(HEADER).decode(FORMAT)
        # msg_length = len(msg_length_b)
        msg = conn.recv(1024)
        cipher = Cipher(algorithms.AES(key), modes.ECB())

        decryptor = cipher.decryptor()
        dt = decryptor.update(msg) + decryptor.finalize()
        d = ""
        for i in dt:
            if i != 0:
                d = d + chr(i) 
        print(f"{addr}: {d}")
        if not msg:
            break
        if msg == "exit":
            connected = False


def get_connection():
    server_soc.listen(5)
    while True:
        conn,addr = server_soc.accept()
        print("BEfore threading")
        thread = threading.Thread(target=handle, args=(conn,addr))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1 }")

get_connection()