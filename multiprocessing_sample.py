# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:05:19 2020

@author: lucky
"""

import multiprocessing
import multiprocessing_support
import time
import os

def sender(conn, msgs): 
	""" 
	function to send messages to other end of pipe 
	"""
	for msg in msgs: 
		conn.send(msg) 
		print("Parent Sent the message: {}".format(msg)) 
	conn.close()

msgs = ["Hi", "How are youe", "I am doing Great", "END"]

parent_conn, child_conn = multiprocessing.Pipe() 

p = multiprocessing.Process(target=multiprocessing_support.worker, args=(child_conn, 1))
p.daemon = True
p.start()

print("Parent process:", os.getpid())

print("Sending data to new process:", p.pid)
sender(parent_conn, msgs)

time.sleep(2)

p.terminate()

p.join()