import math
import sympy

def fib(n):
    fib_list = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b 
        fib_list.append(a)
    return fib_list

def is_palindrome(n : int) -> bool:
    str_form = str(n)
    half_up = math.ceil(len(str_form)/2)
    half_low = int(len(str_form)/2)
    first_half = list(str_form[0:half_up])
    second_half = list(str_form[half_low::])
    second_half.reverse()
    if first_half == second_half:
        return True
    return False

def get_primes_less_than_n(n: int) -> list:
    return list(sympy.sieve.primerange(0,n))

def binary_of_num(n: int) -> int:
    return int(bin(n)[2:])