#Things to look for
# matrix operation
# prime number and gcd
# groups, rings, fields

#so what i found was pycrypto was obsolete no longer maintined.


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


w = open('small.txt', 'rb')
read_file = w.read()
key = b"YELLOW SUBMARINE"

def encrypt_aes(file_content,key):

    padded_bytes = file_content
    bits_added = 0 
    # print(f"1. Origin content(bytes): {file_content}")
    while len(padded_bytes) % 16 != 0:
        padded_bytes = padded_bytes + b'\x00'
        bits_added = bits_added+1
    # print(f"2. Padded bytes: {padded_bytes}")


    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    enrypted_bytes = encryptor.update(padded_bytes) + encryptor.finalize()
    # print(f"3. Encrypted bytes: {enrypted_bytes}")
    value_list = enrypted_bytes
    return enrypted_bytes

c = encrypt_aes(read_file,key)
# print(f"The encrypted version: {c}")



#so the AES is block cipher right? it will work on fix block like 16 bytes so you you make sure you content is either more than 16byte and is not exact mutliple of 16 you need to make it. 

# There are various approach for it likek adding null bytes. adding 1 and zero after than or adding random bytes and at last adding the exact number of how many bytes were added. 
# I did the first one.

# So the concept of doing this is called padding. 
