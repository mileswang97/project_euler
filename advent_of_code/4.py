from itertools import zip_longest, chain
import re

def table_in_ten_lines():
    # represent a table as a set of 5 rows, 5 columns


    return 

with open("inputs/4a.txt", "r") as file:
    lines = file.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].replace("\n", "")
    lines = [line for line in lines if line != '']
    calls = list(eval(lines[0]))
    cards = lines[1::]
    cards = [list(eval(re.sub("\s+", ",", line.strip()))) for line in cards]
    cards = [list(chain(*card)) for card in (grouper(cards, 5))]

def take_a_turn(tables, number):
    # removess number from all table rows and columns.
    # If removing the numbers happens to creates an empty list, you have won.
    
    



def card_wins(card, calls) -> bool:
    overlapping_nums = [num for num in calls if num in card]
    print(overlapping_nums)
    return overlapping_nums

card_wins([49, 0, 9, 90, 8, 41, 88, 56, 13, 6, 17, 11, 45, 26, 75, 29, 62, 27, 83, 36, 31, 78, 1, 55, 38], [0,1,2,3,4,5,6,7])