def twice(f):
    def result(a):
        return f(f(a))
    return result


def plusthree(x):
    return x+3


g = twice(plusthree)

print(g(7))
