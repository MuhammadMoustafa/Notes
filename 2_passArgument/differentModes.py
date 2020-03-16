#https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
#https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/

def parameters(a, b):
    #print(locals())
    return a, b


def defaultParameters(a, b, c=0):
    print(locals())


def manyArgs(*arg):
    print("I was called with", len(arg), "arguments:", arg)

def myfunc(**kwargs):
    # kwargs is a dictionary.
    for k,v in kwargs.items():
         print("%s = %s" % (k, v))


def myfunc2(*args, **kwargs):
   for a in args:
       print("args", a)
   for k,v in kwargs.items():
       print("%s = %s" % (k, v))


# parameters(1, 2)
# defaultParameters(3, 4)
# defaultParameters(3, 4, 5)
# manyArgs(7)
# manyArgs(7, 8)
# manyArgs(7, 8, 9, 10, 11, 12)
# myfunc(abc=123, efh=456)
# myfunc2(1, 2, 3)

# parameters(b=1, a=2)

x = parameters(5 , 8)
print(x)