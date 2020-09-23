# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:05:24 2020

@author: lucky
"""

#https://docs.python.org/2/library/threading.html#threading.Thread.run
#https://dzone.com/articles/python-thread-part-1
#https://dzone.com/articles/python-thread-part-2

import threading
import time

class thread_handler(threading.Thread):
    def __init__(self, threadID, name, run_type):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.daemon = True
        self._running = True
        self.run_type = run_type

    def run(self):
        print("Starting+ " + self.name)

        start_tick(self.run_type)
        time.sleep(2)
        print("Exiting- " + self.name)

    def terminate(self):
        print("Terminate " + self.name)
        self._running = False

def start_tick(run_type):
    print("start_tick:", run_type)
    
    if run_type == 0:
        print("run")
    else:
        print("--:", run_type)

th1 = thread_handler(1, "test", 3)
th1.start()
print("th1", th1.is_alive())

print("th1>>", th1.is_alive())
#th1.join()
th2 = thread_handler(1, "test2", 0)
th2.start()
print("th2", th2.is_alive())
time.sleep(5)
print("th1++", th1.is_alive())
print("th2>>", th2.is_alive())

