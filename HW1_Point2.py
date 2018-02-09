from numpy import *

def esPrimoGaussiano(a,b):
    n = a**2 + b**2
    if (a*b == 0): # así miramos que alguno es 0
        if (abs(int(n**(1/2)))%4 == 3):
            return True
    else:          # acá solo llegan cuando ambos son diferentes de 0
        if esPrimo(n):
            return True
    return False
    
    
def esPrimo(n):  
    ar = arange(2,int(n**(1/2)+1))
    for i in ar:
        if (n%i == 0):
            return False
    return True

arr = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
#Generamos los enteros gaussianos
for i in arr:
    for j in arr:
        if esPrimoGaussiano(i,j):
            x = complex(i,j)
            print(x)
