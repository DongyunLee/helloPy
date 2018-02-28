# coding=utf-8
import threading
import time


def sorry():
    print "我错了"
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread()
