from threading import Thread
from time import sleep,ctime

# 完成这个类
class MyClass(Thread):
    # 该方法可以修改，第8行不能传参数
    def __init__(self,target=None,args=(),kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

# ********************************
# 测试函数，该函数名称，参数都不确定。本函数只提供测试
def player(sec,song):
    for i in range(3):
        print("Playing %s : %s"%(song,ctime()))
        sleep(sec)

t = MyClass(target = player,args=(3,),
            kwargs={'song':'凉凉'})
t.start()
t.join()