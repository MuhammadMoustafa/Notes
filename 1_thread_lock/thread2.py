import threading

lock = threading.Lock()

x = 0 
COUNT = 100000

def adding_2():
    global x
    lock.acquire()
    for i in range (COUNT):
        x += 2
    lock.release()

def adding_3():
    global x
    lock.acquire()
    for i in range (COUNT):
        x += 3
    lock.release()

def subtracting_1():
    global x
    lock.acquire()
    for i in range (COUNT):
        x -= 1
    lock.release()

def subtracting_4():
    global x
    with lock:
        for i in range (COUNT):
            x -= 4


t1 = threading.Thread(target=adding_2)
t2 = threading.Thread(target=adding_3)
t3 = threading.Thread(target=subtracting_1)
t4 = threading.Thread(target=subtracting_4)

t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()

print('x = {}'.format(x))