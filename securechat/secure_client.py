import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

host = "127.0.0.1"
port = 5050
socket_obj_cl  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj_cl.connect((host,port))
key = b"YELLOW SUBMARINE"
while True:
    data = input("> ")
    if data.lower() == "exit":  # Allow "exit" or "EXIT"
        break
    padded_byte = data.encode('utf-8')
    while len(padded_byte) % 16 != 0:
        padded_byte = padded_byte + b'0'
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    enrypted_bytes = encryptor.update(padded_byte) + encryptor.finalize()
    print(f"msg after AES encryption: {enrypted_bytes}")

    socket_obj_cl.sendall(enrypted_bytes)
    # You might want to add a receive loop here if you expect responses from the server

socket_obj_cl.close()

