# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:31:14 2020

@author: lucky
"""

def sender(conn, msgs): 
	""" 
	function to send messages to other end of pipe 
	"""
	for msg in msgs: 
		conn.send(msg) 
		print("Sent the message: {}".format(msg)) 
	conn.close() 

def receiver(conn): 
	""" 
	function to print the messages received from other 
	end of pipe 
	"""
	while 1: 
		msg = conn.recv() 
		if msg == "END": 
			break
		print("Received the message: {}".format(msg)) 

def worker(conn, num):
    """thread worker function"""
    
    while True:
        print('Worker:', num)
        receiver(conn)

        time.sleep(2)
        
    return
