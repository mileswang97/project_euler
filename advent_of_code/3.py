from copy import deepcopy

with open("inputs/3a.txt", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = [int(n) for n in list(lines[index].replace("\n", ""))]

total_lines = len(lines)
length = len(lines[0])

max_bits = length*[0,]

for index in range(length):
    ones = sum(line[index] for line in lines)
    if ones > total_lines/2:
        max_bits[index] = 1

min_bits = [1-n for n in max_bits]

def bin_to_dec(list_of_bits):
    dec = 0 
    for i in range(len(list_of_bits)):
        dec += list_of_bits[-1-i] * 2**(i)
    return dec

#print(bin_to_dec(max_bits) * bin_to_dec(min_bits))

## PART 2
# find oxygen

def find_common_bit_in_index(lines, index, most_or_least=True):
    
    return lines

oxygen_list = deepcopy(lines)
