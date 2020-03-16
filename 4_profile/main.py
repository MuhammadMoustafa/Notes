### https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
### https://docs.python.org/3/library/profile.html#module-cProfile

# from terminal
#   python -m cProfile <your .py file>
# 
# from the program 
#   cprofile.run('<your function>')

#import cProfile

def foo():
    print(50)
    print(51)
    loop()
    pass

def loop():
    for i in range (100000000):
        pass

foo()
#cProfile.run('foo()')


