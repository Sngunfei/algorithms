import threading
import time


def func(lock:threading.Lock, i):
    lock.acquire(blocking=True)
    print("Process {}:\n".format(i))
    for j in range(5):
        print(j)
    time.sleep(5)
    lock.release()
    return


if __name__ == '__main__':
    a = [1, "2"]
    print(a)



