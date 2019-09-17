'''
    分别用单进程 执行10次 count  io,记录时间
    no thread CPU: 7.518454074859619
    no thread IO: 4.570638418197632

   用十个线程每个执行1次 count  io记录时间
   multi Thread CPU: 6.699898958206177
   multi Thread IO: 5.505040168762207

   用十个进程每个执行1次 count  io记录时间
   multi Process CPU: 3.598656415939331
   multi Process io: 2.3045859336853027
'''

"""
测试用例
"""

# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# io
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()

#no thread
# from thread_test import *
# import time
#
# tm = time.time()
# for i in range(10):
#     # count(1,1)
#     io()
# print("no thread IO:",time.time() - tm)

# multi Thread
from thread_test import *
import threading
import time

jobs = []
tm = time.time()
for i in range(10):
    t = threading.Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("multi Thread CPU:",time.time() - tm)

# multi Process
from thread_test import *
import multiprocessing as mp
import time

jobs = []
tm = time.time()
for i in range(10):
    p = mp.Process(target=count,args=(1,1))
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print("multi Process CPU:",time.time() - tm)