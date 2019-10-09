
a=7
print(a)
a=a+1
print(a)
global a
import threading

lock=threading.Lock
lock.acquire()
print(a)
b=a+2
print(b)
