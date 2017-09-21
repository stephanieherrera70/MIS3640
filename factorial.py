import math

def fac(n):
    result = 1
    if n == 1: 
        return result
    print('current n =' , n)
    return n * fac(n - 1)

print(fac(12))


