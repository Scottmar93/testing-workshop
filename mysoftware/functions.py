import numpy as np

def square(x):
    return x*x


def coulomb(r):
    return 1/r

def centralDiff(f, x, h): 
   return (f(x+h) - f(x-h))/(2*h)


    


