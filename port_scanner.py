import socket
import threading
import queue 

host = "www.google.com"
host_ip = socket.gethostbyname(host)
print("The IP is {0}".format(host_ip))

port_range = range(0,65536)

queue_obj = queue.Queue() #creating a que object

num_threads = 64 #thread pool

for port in port_range:
    queue_obj.put(port)

print_lock = threading.Lock()

def scanner():
    while not queue_obj.empty():
        port = queue_obj.get()
        with print_lock:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
        try:
            result = s.connect_ex((host_ip, port))
            with print_lock:
                if result == 0:
                    print(f"Port {port} is open")
        except socket.error as e:
            with print_lock:
                print(f"Error scanning port {port}: {e}")
        finally:
            s.close()

threads=[]

for _ in range(num_threads):
    treads = threading.Thread(target=scanner)
    treads.start()
    threads.append(treads)

for thread in threads:
    thread.join()

print("done")

