import time


def djs(num):
    for i in range(num, 0, -1):
        print("\r倒计时{}秒！".format(i), end="", flush=True)
        time.sleep(1)


def jzjd(num):
    for i in range(num):
        print('\r加载进度: [%-50s]%.2f%%  ' % ('>' * i, i * 1), end='')
        time.sleep(1)



