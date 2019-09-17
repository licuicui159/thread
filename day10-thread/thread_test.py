'''
测试用例
'''
import multiprocessing as mp
from threading import Thread
from timeit import timeit
import time

#计算
def count(x,y):
    c=0
    while c<7000000:
        x+=1
        y+=1
        c+=1
    # else:
    #     print(c)
# @timeit
def io():
    write()
    read()
def write():
    f=open('test','w')
    for i in range(1700000):
        f.write('Hello world\n')
    f.close()
def read():
    f=open('test','r')
    for i in range(1700000):
        f.read()
    f.close()
#单进程执行时长:5.947947
# t=Thread()
# t.start()
# for i in range(10):
#     count(1,1)
# t.join()
# io()

# 创建10个线程执行时长:5.861441
# jobs=[]
# for i in range(10):
#     t=Thread(target=count,args=(1, 1))
#     jobs.append(t) # 存储线程对象
#     t.start()
# for i in jobs:
#     i.join()
# io()

# 创建10个进程执行时长:5.528384
# jobs=[]
# for i in range(10):
#     p=mp.Process(target=count,args=(1, 1))
#     jobs.append(p) # 存储线程对象
#     p.start()
#
# for i in jobs:
#     i.join()
# io()

start_time=time.time()
jobs=[]
for i in range(10):
    p=mp.Process(target=io)
    jobs.append(p)
    p.start()
end_time=time.time()

for i in jobs:
    i.join()

print(end_time-start_time)
