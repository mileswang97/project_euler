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

def filter_lines_by_index(lines, index, most_or_least=True):
    lines_count = len(lines)
    if lines_count == 1:
        return lines
    ones = sum(line[index] for line in lines)
    keep_ones = ones >= lines_count/2
    if most_or_least:
        return [line for line in lines if line[index] == keep_ones]
    else:
        return [line for line in lines if line[index] != keep_ones]

oxygen_list = deepcopy(lines)
coo_scrubber_list = deepcopy(lines)

for index in range(length):
    oxygen_list = filter_lines_by_index(oxygen_list, index, most_or_least=True)

print(oxygen_list)

for index in range(length):
    coo_scrubber_list = filter_lines_by_index(coo_scrubber_list, index, most_or_least=False)

print(coo_scrubber_list)

print(bin_to_dec(oxygen_list[0]) * bin_to_dec(coo_scrubber_list[0]))