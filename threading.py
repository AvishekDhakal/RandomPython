# so the threading and queue module are use in conjunction.

# queue is the implementation of FIFO (First in first out) its simple.

from threading import Thread
from queue import Queue
import threading
import time

num_range = range(10000000)
starttime = time.localtime()
print("starting from {0}:{1}:{2}".format(starttime[3], starttime[4], starttime[5]))

q = Queue()
for num in num_range:
    q.put(num)

print_lock = threading.Lock()
threadsnum = 64

def printing():
    while not q.empty():
        number = q.get()
        print(number)

treads = []

for _ in range(threadsnum):
    threads = Thread(target=printing)
    threads.start()
    treads.append(threads)
for thread in treads:
    thread.join()

endtime = time.localtime()

print("ending in {0}:{1}:{2}".format(endtime[3], endtime[4], endtime[5]))
print("done")