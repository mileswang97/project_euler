"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.

For example, 28 is a perfect number: 1 + 2 + 4 + 7 + 14 = 28.
Called deficient if sum is below, abundant if sum is above. 

12 is the smallest abundant number, and 24 is the smallest number that can be written as the sum of 2 abundant numbers.
By analysis, it can be shown that any number above 28123 can be written as the sum of two abundant numbers. However this upper limit cannot 
be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all positive integers that cannot be written as the sum of two abundant numbers.
"""

from utils.utils import *
from utils.sequences import *

problem_list = range(1, 28124)

sum_divisors_list = [sum_of_divisors(i) for i in problem_list]
abundant_list = [i for i in problem_list if i < sum_divisors_list[i-1]] 

#print(abundant_list)
# 12, 18, 20, 24, 30

sum_of_two_abundants = possible_sums_from_two_lists(abundant_list, abundant_list)
not_sum_of_two_abundants = [i for i in problem_list if i not in sum_of_two_abundants]

print(sum(not_sum_of_two_abundants))

# 4179871