"""
模拟开启多个线程，在多资源情况下共同下载一个文件
"""
import os
from threading import Thread,Lock
from time import sleep

urls = ["/home/tarena/桌面/",
"/home/tarena/文档/",
"/home/tarena/音乐/",
"/home/tarena/下载/",
"/home/tarena/视频/",
"/home/tarena/图片/",
"/home/tarena/模板/",
]

lock = Lock() # 锁

filename = input("要下载的文件:")
explorer = []
for i in urls:
    # 判断资源库路径中文件是否存在
    if os.path.exists(i+filename):
        # 存文件路径
        explorer.append(i+filename)

num = len(explorer) # 获取有多少资源
if num == 0:
    print("没有资源")
    os._exit(0)
size = os.path.getsize(explorer[0])
block_size = size // num + 1

# 共享资源
fd = open(filename,'wb') # 下载的文件

# 下载文件
def load(path,num):
    f = open(path,'rb') # 从资源中读取内容
    seek_types = block_size * num
    f.seek(seek_types)
    size = block_size

    lock.acquire() # 上锁
    fd.seek(block_size * num)
    while True:
        # sleep(0.1)
        if size < 1024:
            data = f.read(size)
            fd.write(data)
            break
        else:
            data = f.read(1024)
            fd.write(data)
            size -= 1024
    lock.release()

n = 0  # 给每个线程分配的是第几块
jobs = []
for path in explorer:
    t = Thread(target = load,args=(path,n))
    jobs.append(t)
    t.start()
    n += 1

for i in jobs:
    i.join()

