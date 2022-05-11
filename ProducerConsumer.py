from threading import Thread, Semaphore
import time
import random
from queue import Queue
# defining the buffer size
MAX_SIZE = 10
q = Queue(maxsize=MAX_SIZE)

sem = Semaphore()


class ProducerClass(Thread):
    def run(self):
        global q
        while True:
            sem.acquire()  # acquires the lock to produce items
            # now check , whether buffer is empty or not
            if(q.qsize() == MAX_SIZE):
                # means buffer is full, cannot generate a random number and insert in buffer
                print("Buffer is Already Full! Waiting for the Consumer to Consume!")
                sem.release()

            # otherwise.....
            r1 = random.randint(1, 100)  # created a Random Number...
            q.put(r1)
            print("Producer produced : ", r1)
            sem.release()
            time.sleep(0.3)


class ConsumerClass(Thread):
    def run(self):
        global q
        while True:
            sem.acquire()
            if(q.qsize() == 0):
                print("Buffer is Empty! Cannot Consume Items!")
                sem.release()

            # otherwise...
            current = q.get()
            print("Item Consumed is : ", current)
            sem.release()
            time.sleep(random.random())


def main():
    ProducerClass().start()
    ConsumerClass().start()


main()
