#from analyticsvidhya


# simple code
# start of program >> sleepy_man() >> sleepy_man >> print function for time taken >> end of program

import time
def sleepy_man():
    print('Starting to sleep')
    time.sleep(1)
    print('Done sleeping')

tic = time.time() #returns the number of seconds passed since epoch.
sleepy_man()
sleepy_man()
toc = time.time() #secs from epoch again but after completed 2 functions bove
print('Done in {:.4f} seconds'.format(toc-tic))

# Multi-Processing the code.
#https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/
