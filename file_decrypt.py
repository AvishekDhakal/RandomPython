
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from file_encrypt import encrypt_aes 


key = b"YELLOW SUBMARINE"
# encrypted_byte = b'\x1a\xf9r]\xd4\xeb7\x08XX1\x05\x13\xe3\xfd\x05Q\x85\xe5MZy\x80y\x90p\xa4\x8e$\x80|\x89'
my_message = b'shh! It\'s secret.' 
encrypted_byte = encrypt_aes(my_message, key)
print(f"enc: {encrypted_byte}")

cipher = Cipher(algorithms.AES(key), modes.ECB())

decryptor = cipher.decryptor()
dt = decryptor.update(encrypted_byte) + decryptor.finalize()
print(dt)
d = ""
for i in dt:
    if i != 0:
        d = d + chr(i) 
print(d)
print(len(d))
