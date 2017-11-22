# -*- coding: utf-8 -*-
"""
参考链接：http://www.cnblogs.com/fnng/p/3670789.html
"""

# --单线程例子-- #
# from time import sleep, ctime, time
#
#
# def listenMusic(func):  # 听5次歌，每次用2秒
#     for i in range(5):
#         print('我正在听 %s, 现在的时间是 %s' % (func, ctime()))
#         sleep(2)
#
# def watchMovie(func):  # 看2次电影，每次用3秒
#     for i in range(2):
#         print('我正在看 %s, 现在的时间是 %s' % (func, ctime()))
#         sleep(3)
#
# if __name__ == '__main__':
#     time_start = time()
#     listenMusic('追光者')
#     watchMovie('阿凡达')
#     time_end = time()
#     print('完成所有动作的时间 %s秒' % (time_end-time_start))


# --多线程例子-- #
import threading
from time import ctime, sleep, time

def listenMusic(func):  # 听5次歌，每次用2秒
    for i in range(5):
        print('我正在听 %s, 现在的时间是 %s' % (func, ctime()))
        sleep(2)

def watchMovie(func):  # 看2次电影，每次用3秒
    for i in range(2):
        print('我正在看 %s, 现在的时间是 %s' % (func, ctime()))
        sleep(3)

threads = []  # 创建了threads数组
t1 = threading.Thread(target=listenMusic, args=(u'蜗牛', ))  # 创建线程t1,使用threading.Thread()方法，在这个方法中调用listenMusic方法,args方法对listenMusic进行传参。
threads.append(t1)  # 把创建好的线程t1装到threads数组
t2 = threading.Thread(target=watchMovie, args=(u'攻守道',))
threads.append(t2)

if __name__ == '__main__':
    time_start = time()
    for j in threads:  # 通过for循环遍历数组。（数组被装载了t1和t2两个线程）
        j.setDaemon(True)  # setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
        # 如果不设置为守护线程程序会被无限挂起。线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。
        j.start()  # 开始线程活动。
    j.join()
    time_end = time()
    print('完成所有动作的时间 %s秒' % (time_end - time_start))

