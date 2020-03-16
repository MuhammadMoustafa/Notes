import threading

x = 0 
COUNT = 100000

def adding_2():
    global x
    for i in range (COUNT):
        x += 2
    
def adding_3():
    global x
    for i in range (COUNT):
        x += 3
    
def subtracting_1():
    global x
    for i in range (COUNT):
        x -= 1
    
def subtracting_4():
    global x
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

'''
adding_2()
adding_3()
subtracting_1()
subtracting_4()
'''
print('x = {}'.format(x))