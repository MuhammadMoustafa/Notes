'''
The timing metrics for methods can show you statistics, such as 
the number of calls (shown as ncalls), 
total time spent in the function (tottime), 
time per call (tottime/ncalls and shown as percall), 
cumulative time spent in a function (cumtime), 
and cumulative time per call (quotient of cumtime over the number of primitive calls and shown as percall after cumtime).

When there are two numbers in the first column (for example 3/1 ), 
it means that the function recursed.
The first is the total number of calls.
The second value is the number of primitive calls 
'''
import numpy as np

input1 = np.array(range(1000000))
input2 = np.array(range(1000000))
output = np.array(range(1000000))

def vect():
    output = input1 + input2
    return output

def nonVect():
    for i in range(len(input1)):
        output[i] = input1[i] + input2[i]

    return output


vectOut = vect()
nonVectOut = nonVect()

print(vectOut)
print(nonVectOut)