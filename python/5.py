from typing import final
import sympy
import numpy as np

#prime_list = list(sympy.sieve.primerange(0,20))

"""
def merge_dicts(dict1 : dict, dict2 : dict) -> dict:
    final_dict = dict1
    for key in dict2.keys():
        if key not in final_dict.keys():
            final_dict[key] = dict2[key]
        else:
            if dict2[key] > final_dict[key]:
                final_dict[key] = dict2[key]
    return final_dict

def prime_factor_tree(n: int) -> dict:
    prime_factors = []
    while n > 1:
        for prime in prime_list:
            if n % prime == 0:
                prime_factors.append(prime)
                n = n / prime
                continue
    prime_factors_dict = {}
    for value in prime_factors:
        if value not in prime_factors_dict.keys():
            prime_factors_dict[value] = 1
        else:
            prime_factors_dict[value] += 1
    return prime_factors_dict 

# find list of prime factors that contain every element
def prime_factors_list(n: int) -> list:
    n_range = np.arange(2, n+1)
    master_tree = dict()
    for i in n_range:
        i_dict = prime_factor_tree(i)
        master_tree = merge_dicts(master_tree, i_dict)
    print(master_tree)
    return
"""

def largest_prime_power(prime, n):
    prime_power = prime
    extend_list = []
    while prime_power*prime < n:
        extend_list.append(prime)
        prime_power = prime_power*prime
    return extend_list

# much better way
def prime_factors_list(n: int) -> list:
    prime_list = list(sympy.sieve.primerange(0,n+1))
    master_list = list(sympy.sieve.primerange(0,n+1))
    for prime in prime_list:
        extend_list = largest_prime_power(prime, n)
        master_list.extend(extend_list)
    master_list = sorted(master_list)
    return master_list

prod = 1
for value in prime_factors_list(20):
    prod = prod * value
print(prod)