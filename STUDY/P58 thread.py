#  thread = a flow of execution. Like a separate order of instructions.
#           However each thread takes a turn running to achieve concurrently (одновременнo)
#           GIL = (global interpreter lock)
#           allows only one thread to hold the control of the Python interpreter at one time

#  cpu bound = program/task spends most of its time waiting for internal events (внутренние события) (CPU intensive)
#               use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#               use multithreading

import threading
import time

# Each of these task below are io bound
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

#thread synchronization
#x.join()
#y.join()
#z.join()


# How to check te number of threads that are currently running in the background
print(threading.active_count())
# How to print a list of function that are running
print(threading.enumerate())
print(time.perf_counter())

#from GG
# Python program to illustrate the concept of threading importing the threading module
import threading

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")