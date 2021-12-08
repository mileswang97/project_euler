with open("inputs/1a.txt", "r") as file:
    templist = list()
    lines = file.readlines()
    for line in lines:
        templist.append(int(line))

#print(templist)

truth_array = [(templist[i+1] > templist[i]) for i in range(len(templist)-1)]

#print(truth_array)

#print(sum(truth_array))

sliding_window_truth_array = [(templist[i+3] > templist[i]) for i in range(len(templist)-3)]

print(sum(sliding_window_truth_array))