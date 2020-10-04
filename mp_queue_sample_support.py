# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:22:02 2020

@author: lucky
"""


from multiprocessing import Process, Queue
import time
import os
import datetime

def get_cmd(queue):
    ## Read from the queue; this will be spawned as a separate Process
    try:
        msg = queue.get(block=False)         # Read from the queue and do nothing
        print("<<<", msg)
        return msg
    except Exception as e:
        print("Exception")
        print(e)
        return None


def put_cmd(queue, cmd):
    ## Write to the queue
    queue.put(cmd)             # Write 'count' numbers into the queue
    
def start_queue(queue, li):

    print(li)
    
    while True:
        
        ts1 = datetime.datetime.now().timestamp()
        print("ts1:", ts1)

        msg = get_cmd(queue)
        ts2 = datetime.datetime.now().timestamp()
        print("ts2:", ts2)

        diff = ts2 - ts1
        print("diff:", diff)


        if msg:
            if (msg == 'END'):
                break
        
        #time.sleep(1)
        print("waiting...")
    
