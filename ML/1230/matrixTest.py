import numpy as numpy


a=numpy.matrix([[1,3],[4,0]])
b=numpy.matrix([[3],[1]])
print(a * b)
c=a.getI()
d=a.getT()
print("***********")
print(c)
print(d)