# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:12:51 2020

@author: lucky
"""


from multiprocessing import Process, Queue
import mp_queue_sample_support
import time
import os

g_queue = None


def start_ticker():
    msgs = ["Hi", "How are youe", "I am doing Great"]
    
    g_queue = Queue()
    
    p = Process(target=mp_queue_sample_support.start_queue, args=((g_queue),))
    p.daemon = True
    p.start()
    
    print("Parent process:", os.getpid())

    print("Sending data to new process:", p.pid)
    
    for msg in msgs:
        print(">>>>", msg)
        mp_queue_sample_support.put_cmd(g_queue, msg)
        
    time.sleep(1)

    print(">>>>", "END")
    mp_queue_sample_support.put_cmd(g_queue, "END")

    g_queue.close()
    
    p.terminate()

    p.join()

start_ticker()
