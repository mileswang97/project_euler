import math
import numpy as np

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

def largest_palindrome(num_digits: int = 3) -> int:
    a_list = np.arange(10**(num_digits-1), 10**num_digits)
    b_list = np.arange(10**(num_digits-1), 10**num_digits)
    palin_list = []
    for i in a_list:
        for j in b_list:
            prod = i*j
            if is_palindrome(prod):
                palin_list.append(prod)
    palin_list = sorted(palin_list)
    print(palin_list[-1])
    return

largest_palindrome()