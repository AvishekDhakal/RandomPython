import requests
from time import sleep
import queue
import threading


dir = open('medium.txt', 'r')
words = []

q = queue.Queue()

for word in dir:
       q.put(word.strip())

print_lock = threading.Lock()
threadsnum = 32

results = []
def bruteforce():
    counter = 1
    try:
        while not q.empty():
                i = q.get()
                url = "https://httpbin.org/" + i
                url = "http://172.16.145.130/" + i

                response = requests.get(url)
                print(f"{counter} URL: {url}  status-code{response.status_code}")
                counter = counter + 1
                if response.status_code == 200:
                    results.append(url)
    except ConnectionResetError as e:
         print("Facing issues but will continues",e)
         sleep(4)
    except requests.exceptions.ConnectionError as  e:
         print("Facing issues but will continues",e)
         sleep(4)
         
treads = []

for _ in range(threadsnum):
    threads = threading.Thread(target=bruteforce)
    threads.start()
    treads.append(threads)
for thread in treads:
    thread.join()

for i in results:
       print(f"{i} is 200/OK")
