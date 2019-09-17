"""
死锁情形模拟
"""
from threading import Thread,Lock
from time import sleep

# 账户类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id  # id
        self.balance = balance  # 存款
        self.lock = lock # 维护锁

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount
    # 存钱
    def deposit(self,amount):
        self.balance += amount
    # 查看余额
    def get_balance(self):
        return self.balance

# 生成两个账户
Tom = Account('Tom',12000,Lock())
Abby = Account('Abby',9000,Lock())

# 转账  账户金额变动需要先上锁
def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount) # from_账户钱减少
        sleep(0.1)
        if to.lock.acquire():
            to.deposit(amount) # to 存钱
            to.lock.release()
        from_.lock.release()
    print("%s给%s转了%d元"%(from_.id,to.id,amount))

t1 = Thread(target=transfer,args=(Tom,Abby,4000))
t2 = Thread(target=transfer,args=(Abby,Tom,1500))
t1.start()
t2.start()
t1.join()
t2.join()
print("Tom:",Tom.get_balance())
print("Abby:",Abby.get_balance())