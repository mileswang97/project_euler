import numpy as np

triangle= [
    [75,],
    [95,64,],
    [17,47,82,],
    [18,35,87,10,],
    [20,4,82,47,65,],
    [19,1,23,75,3,34,],
    [88,2,77,73,7,63,67,],
    [99,65,4,28,6,16,70,92,],
    [41,41,26,56,83,40,80,70,33,],
    [41,48,72,33,47,32,37,16,94,29,],
    [53,71,44,65,25,43,91,52,97,51,14,],
    [70,11,33,28,77,73,17,78,39,68,17,57,],
    [91,71,52,38,17,14,91,43,58,50,27,29,48,],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31,],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23,],
]

# teddy said something about dynamic programming

# Let's think about this way: 

"""
Suppose we are at row N, where there are N points. To draw a path "upwards", 
there are technically 2(n-1) possible paths, but only (n-1) are known to be viable (potentially optimal)
because the other path that connects to the same index in (n-1) is guaranteed to be worse.

If we write a program that starts at the bottom row, and store optimal paths incrementally, there should
be at most 2n(n+1) computations. (or just (n-1)(n-2)???)
"""

from typing import Iterable

from numpy.core.defchararray import array

def increment_path(
    array_previous: Iterable,
    current_row: list,
) -> Iterable:
    array_next = np.zeros(len(current_row))
    for i in range(len(array_next)):
        a = array_previous[i]
        b = array_previous[i+1]
        num_to_add = a if a > b else b
        array_next[i] = current_row[i] + num_to_add
    return array_next

def main(triangle=triangle):
    array_previous = np.zeros(len(triangle) + 1)

    for i in list(reversed(range(len(triangle)))):
        array_next = increment_path(
            array_previous=array_previous,
            current_row=triangle[i],
        )
        array_previous = array_next
    
    print(array_next)

main()