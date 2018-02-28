# coding=utf-8
import threading

# 当用继承创建线程时要重写run()
# 1、每个线程一定会有一个名字
# 2、当run方法结束的时候，线程也结束
# 3、人为无法完全控制线程，调度由操作系统控制
#    但是可以通过一些方式来影响调度：互斥锁/sleep/死锁(线程互相抢夺资源，停止运行)
# 4、线程的状态：新建=>就绪=>（等待态/阻塞）=>运行=>死亡
import time

"""
class MyThreading(threading.Thread):
    def run(self):
        for i in range(5):
            a = '线程' + self.name + str(i)
            print a
            time.sleep(1)


if __name__ == '__main__':
    t = MyThreading()
    t.start()
"""

num = 0


class MyThread(threading.Thread):
    def run(self):
        # 告诉py解释器，将对全局变量进行修改
        global num
        num = num + 1
        time.sleep(1)
        print self.name + 'set num to ' + str(num)


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == "__main__":
    test()
