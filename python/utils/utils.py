import math
import numpy as np
from utils.sequences import squares

def is_square(n: int) -> bool:
    list_of_squares = squares((n+1)/2)
    return n in list_of_squares

def is_palindrome(n: int) -> bool:
    str_form = str(n)
    half_up = math.ceil(len(str_form)/2)
    half_low = int(len(str_form)/2)
    first_half = list(str_form[0:half_up])
    second_half = list(str_form[half_low::])
    second_half.reverse()
    if first_half == second_half:
        return True
    return False

def binary_of_num(n: int) -> int:
    return int(bin(n)[2:])

def list_of_divisors(n: int) -> list:
    sq_rt = math.sqrt(n)
    divisor_list = list()

    half_list = np.arange(1, int(sq_rt)+1)
    for i in half_list:
        if n % i == 0:
            divisor_list.append(i)
            if not(i == sq_rt):
                divisor_list.append(int(n/i))

    return sorted(divisor_list)