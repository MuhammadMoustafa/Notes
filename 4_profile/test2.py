# Element-wise multiplication 
import time 
import numpy 
import array 
  
a = array.array('i') 
for i in range(50000): 
    a.append(i); 
  
b = array.array('i') 
for i in range(50000, 100000): 
    b.append(i) 
  
# classic element wise product of vectors implementation  
vector = numpy.zeros((50000)) 
  
tic = time.process_time() 
  
for i in range(len(a)): 
      vector[i]= a[i]*b[i] 
  
toc = time.process_time() 
  
print("Element wise Product = "+ str(vector)); 
print("\nComputation time = "+str(1000*(toc - tic ))+"ms") 
   
  
n_tic = time.process_time() 
vector = numpy.multiply(a, b) 
n_toc = time.process_time() 
  
print("Element wise Product = "+str(vector)); 
print("\nComputation time = "+str(1000*(n_toc - n_tic ))+"ms") 