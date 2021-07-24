import math
import typing

def solution(n: int):
    n_list = range(1,n)
    three_set = set(filter(lambda x: x % 3 == 0, n_list))
    five_set = set(filter(lambda x: x % 5 == 0, n_list))
    union = three_set.union(five_set)
    return sum(union)

print(solution(1000))

print(solution(10))

