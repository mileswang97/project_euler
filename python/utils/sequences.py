import sympy
import numpy as np
from itertools import accumulate

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

def triangles(n: int) -> list:
    return list(accumulate(range(1, n+1)))

def possible_sums_from_two_lists(a_list: list, b_list: list): 
    sum_set = set()
    if a_list == b_list:
        for index in range(len(a_list)):
            sums = [a_list[index] + b_list[i] for i in range(index, len(b_list))]
            for sum in sums:
                sum_set.add(sum)
        return sum_set
    else:
        for index in range(len(a_list)):
            sums = [a_list[index] + b_list[i] for i in range(len(b_list))]
            for sum in sums:
                sum_set.add(sum)
        return sum_set