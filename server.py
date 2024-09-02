import socket

host = '127.0.0.1'
port = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
with conn:
    print("The connection is", addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
        print(data)



# Echo server program
# import socket

# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     (s.bind((HOST, PORT))) # This bind shit is nothign but just binding or tying together the socket we created with the host and port we want. 
#     s.listen(0)
#     conn, addr = s.accept()
#     print(conn)
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data: break
#             d = data + b' what up' 
#             conn.sendall(d)


#The AF stand for address family and SOCK stands for SOCKETKIND.

# socket.SOCK_STREAM -- for tcp
# socket.SOCK_DGRAM -- for udp


# accept()
# bind()
# connect()
# connect_ex()) 
# close()
# s.listen()
#recv()

# send()    A slight difference between these two. this one sends how much data server can handle. it returns the numbmer of data sent
# send_all() while this one sneds all the data it nesds to send no matter what only stops on error.

# Received b'Hell what upo, w what uporld what up' -- this was when i sent using send. The server accepted 4 bytes so echoed 4 bytes.

# Received b'Hell what up' and this is when i sent using send_all. its like udp sending data wont stop for server.


# A server should always follow sbla 

# socket, bind, listen, accept

# the accept returns 2 value connc and addr
# the conn is us and addr is the connected server.

#the serever accpets the values by using the conn

# SBlA