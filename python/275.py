import math
# for n > 2

# X(n) = summation of X(n-2) * (height choose 2)

"""
def balanced_sculptures(n, blocks=0):
    #count=0
    #base_case, all blocks straight up
    if blocks == 0:
        count += 1
    # -2 from middle "spine"
    balanced_sculptures(n-2, 2)
"""


# Brute Force method
#form of structure:
# [(x, y), ...]

def create_all_structures(n):
    # blocks have to all be connected to each other
    solution_set = set()
    structure = [(0,0), (0,1)]
    for i in range(n-1):
        # add a block to the structure
        print("pepelaugh")
    if is_balanced(structure):
        reflection = [(-a, b) for (a, b) in structure]
        if reflection not in solution_set:
            solution_set.add(structure)
    return solution_set

def is_balanced(structure):
    x_list = [a for (a, b) in structure]
    numblocks = len(structure)
    center = sum(x_list) / numblocks
    if (center, 0) in structure:
        return True
    return False

pass_struct = [(0,0), (0,1), (0,2), (1,0), (2,0), (3,0)]
print("pass", is_balanced(pass_struct))

fail_struct = [(0,0), (0,1), (0,2), (1,0), (2,0), (3,0)]


"""
elegant method thoughts

lets count the number of structures by summing
over different middle spine lengths. so X(n) = 
s(1)(n-1) + s(2)(n-2) ...

There can't be any variation in the spine (has to be 
one column up in center) so it's a question of distributing
the remaining n-k cubes on a number scale from -inf,-1 to 1,inf
such that the following conditions are met:

1) if a block is in position +/- m, there has to be 
at least one block in each of positions +/- 1, 2 ... m-1
2) the position each initial block in each x-coordinate is upper-bound
limited by the height of the spine (and some combination of the previous blocks)
    a) each block in that x-coordinate after the initial block has 
"""


"""
elegant pythonic thoughts

have initial block start at (0,0) [first block, NOT the plinth].
Each block after can go up one (+1, 0) or right one (0, +1). There should
be a way to iterate through the entire solution space.

Find the center of mass. It should be a whole number. If its not, doesn't work.

Look at the index of the center of mass. Is there a block with (M, 0)?
If not, doesn't work.

PROBLEM: some shapes cannot be created (do not have lower left starting block)
"""

#print(generate_binary(2))

def special_add(structure_set: set, structure):
    positional_variations = []
    for i in range(10):
        for j in range(10):
            new_structure_add = [(a+i, b+j) for (a,b) in structure]
            new_structure_minus = [(a-i, b-j) for (a,b) in structure]
            positional_variations.append(new_structure_minus)
            positional_variations.append(new_structure_add)
    