with open("inputs/4a.txt", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].replace("\n", "")

print(lines)