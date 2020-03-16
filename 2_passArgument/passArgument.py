#By value or By Refernece?
#https://stackoverflow.com/questions/13299427/python-functions-call-by-reference


def clear_a(x):
  x = []

def clear_b(x):
  while x: x.pop()

z = [1,2,3]
clear_a(z) # z will not be changed
print(z)
clear_b(z) # z will be emptied
print(z)


#return more than one value
# def foo(x, y):
#    return x**2, y**2

# a = 1
# b = 2
# a, b = foo(a, b)  # a == 2; b == 4
# print("a, b", a, b)
