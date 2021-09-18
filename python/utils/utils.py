import math


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

def binary_of_num(n: int) -> int:
    return int(bin(n)[2:])