# Taken from 18

from typing import Iterable
import numpy as np
from numpy.core.defchararray import array

with open("files/p067_triangle.txt", "r") as file:
    triangle = file.readlines()
    for i in range(len(triangle)):
        line = triangle[i]
        line = line.replace("\n", "")
        line = line.split(" ")
        line = [int(i) for i in line]
        triangle[i] = line


def increment_path(
    array_previous: Iterable,
    current_row: list,
) -> Iterable:
    array_next = np.zeros(len(current_row))
    for i in range(len(array_next)):
        a = array_previous[i]
        b = array_previous[i + 1]
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
