# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:22:02 2020

@author: lucky
"""


from multiprocessing import Process, Queue
import time
import os


def get_cmd(queue):
    ## Read from the queue; this will be spawned as a separate Process
    msg = queue.get()         # Read from the queue and do nothing
    print(msg)
    return msg


def put_cmd(queue, cmd):
    ## Write to the queue
    queue.put(cmd)             # Write 'count' numbers into the queue
    
def start_queue(queue):
    
    while True:
        msg = get_cmd(queue)

        if (msg == 'DONE'):
            break
        
        #time.sleep(1)
        print("waiting...")