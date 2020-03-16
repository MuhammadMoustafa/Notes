def printText(text):
    print(text)


def b(func, args):
    func(args)


def main():
    #b(a, "Muhammad")

    '''
    decorated_b = decorator(printText, "Muhammad")
    decorated_b()
    '''


    add_one = create_adder(1)
    add_two = create_adder(2)
    print(add_one(9))
    print(add_two(11))



def decorator(func, args):
    def wrap():
        print("********")
        func(args)
        print("********")
    return wrap


def create_adder(x):
    def adder(y):
        return x+y
    return adder


if __name__ == "__main__":
    main()


'''
Closure
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 

higher order function
In mathematics and computer science, a higher-order function is a function that does at least one of the following: 
takes one or more functions as arguments,
returns a function as its result.


currying
In mathematics and computer science, currying is the technique of translating the evaluation of a function that takes multiple arguments 
into evaluating a sequence of functions, each with a single argument. For example, a function that takes two arguments, one from X and one from Y, 
and produces outputs in Z, 
by currying is translated into a function that takes a single argument from X and produces as outputs functions from Y to Z.
'''
