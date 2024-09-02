

text = b'HELLO WORLD'
key = b'ICEICEIICEIC'
cipher = b'\x01\x06\t\x05\x0ce\x1e\x06\x11\t\r'
# cipher = b'\x01\x06\t\x05\x0ce\x1e\x06\x11\t('

f = bytes([b1 ^ b2 for b1 , b2 in zip(cipher, key)])
print(f)






