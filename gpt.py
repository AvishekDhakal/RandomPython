import socket
import threading
from queue import Queue

# Define the target host
host = 'www.google.com'
host_ip = socket.gethostbyname(host)
print("The host IP is:", host_ip)

# Define the port range to scan
port_range = range(20, 101)

# Create a queue to manage the ports
port_queue = Queue()

# Fill the queue with ports
for port in port_range:
    port_queue.put(port)

# Define the number of threads
num_threads = 10

# Define a lock for printing to avoid jumbled output
print_lock = threading.Lock()

# Define the worker function
def port_scanner():
    while not port_queue.empty():
        port = port_queue.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((host_ip, port))
            with print_lock:
                if result == 0:
                    print(f"Port {port} is open")
                else:
                    print(f"Port {port} is closed")
        except socket.error as e:
            with print_lock:
                print(f"Error scanning port {port}: {e}")
        finally:
            s.close()
            port_queue.task_done()

# Create and start threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=port_scanner)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Port scanning completed.")





