with open("inputs/2a.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = tuple(lines[i].replace('\n', '').split(' '))
    print(lines)

depth_counter = 0
hor_counter = 0

for line in lines:
    if line[0] == 'forward':
        hor_counter += int(line[1])
    if line[0] == 'up':
        depth_counter = depth_counter - int(line[1])
    if line[0] == 'down':
        depth_counter += int(line[1])

# part 1
# print(hor_counter * depth_counter)


# part 2

aim_counter = 0
hor_counter = 0
depth_counter = 0

for line in lines:
    if line[0] == 'forward':
        hor_counter += int(line[1])
        depth_counter += int(line[1])  * aim_counter
    if line[0] == 'up':
        aim_counter = aim_counter - int(line[1])
    if line[0] == 'down':
        aim_counter += int(line[1])

print(hor_counter * depth_counter)