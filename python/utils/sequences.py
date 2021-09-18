import sympy
import numpy as np

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b 
        fib_list.append(a)
    return fib_list

def primes(n: int) -> list:
    return list(sympy.sieve.primerange(0,n))

def squares(n: int) -> list:
    return list(np.square(np.arange(1,n+1)))

def powers(n: int, p: int) -> list:
    return list(np.power(np.arange(1,n+1), p))

