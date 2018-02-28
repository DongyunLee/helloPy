# coding=utf-8
# 同步
# 当一个线程调用锁的acquire方法时获得锁，锁会进入上锁状态
# 每次只有一个线程可以获得锁，如果此时另外一个线程试图获得这个锁时，该线程会阻塞
# 直到拥有锁的线程调用了release方法释放锁之后，其他线程才能够获得这把锁

# 好处：确保了某段关键代码只能由一个线程从头到尾执行，保证了数据的唯一性

# 用了锁之后，程序会变成单线程
# 坏处：阻止了多线程并发执行，效率大大降低
#       由于可以存在多个锁，当不同的线程持有不同的锁，并试图获取对方的锁时，可能造成死锁

# tips：尽量少用全局变量，不安全

# 高并发服务器：web开发、区块链
import threading
import time

num = 0
lock = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        # 锁住变量
        flag = lock.acquire()
        msg = "线程的锁(%s)状态为%d" % (self.name, flag)
        print msg
        # 判断是否上锁成功
        if flag:
            num = num + 1
            time.sleep(1)
            msg = self.name + ' set num to ' + str(num)
            print msg
            lock.release()


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == "__main__":
    test()
