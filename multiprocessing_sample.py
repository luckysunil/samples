# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:05:19 2020

@author: lucky
"""

import multiprocessing
import multiprocessing_support
import time

p = multiprocessing.Process(target=multiprocessing_support.worker, args=(1,))
p.start()

time.sleep(2)

p.terminate()