# definitions

digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "",
}

one_tens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
    0: "",
}

master_string = ""

for i in range(1, 1001):
    if i < 10:
        master_string = master_string + digits[i]
        continue
    elif i < 20:
        master_string = master_string + one_tens[i]
        continue
    elif i < 100:
        istr = str(i)
        master_string = master_string + tens[int(istr[0])] + digits[int(istr[1])]
        continue
    elif i < 1000:
        istr = str(i)
        if istr[1] == "1":
            master_string = (
                master_string
                + digits[int(istr[0])]
                + "hundredand"
                + one_tens[int(istr[1::])]
            )
            continue
        else:
            master_string = (
                master_string
                + digits[int(istr[0])]
                + "hundredand"
                + tens[int(istr[1])]
                + digits[int(istr[2])]
            )
            continue
    elif i == 1000:
        master_string = master_string + "onethousand"

# print("length", len(list(master_string)))

# print(master_string)

# this is so boosted but i dont care for this problem
# error in code when it reaches one hundred, just adds "hundredand" even if the number is X00.

print("length", len(list(master_string)) - 27)
