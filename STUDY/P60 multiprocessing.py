# Python multiprocessing

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num): #create the function that count from 0 to certain number which we will pass later as an argumet
    count = 0
    while count < num:
        count += 1

def main():

    print("cpu count:", cpu_count()) #chaeck how many additional processe u can run
# divide between 2 processes
    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    a.start()
    b.start()

    print("processing...")

#In order to execute the rest of the program after the multi-process functions are executed,
    # we need to execute the function join().
    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")

# note!: if u create a child process
if __name__ == '__main__':
    main()

