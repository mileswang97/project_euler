from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

with open("inputs/4a.txt", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].replace("\n", "")
    lines = [line for line in lines if line != '']
    calls = lines[0]
    cards = lines[1::]

cards = list(grouper(cards, 5))

def array_like(n_tuple):

    return 

print(cards)