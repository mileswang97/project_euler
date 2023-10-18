from utils.sequences import squares

# 44722, 3163

b_squares = squares(3163)
# b_squares = squares(44722)


def set_of_sums_less_than_n(
    n: int,
    lista: list,
    listb: list,
    factors: tuple([int, int]),
) -> set:
    result = set()

    for a in lista:
        for b in listb:
            num = factors[0] * a + factors[1] * b
            if num < n and num not in result:
                result.add(num)
    return result


a1_1 = set_of_sums_less_than_n(10000000, b_squares, b_squares, (1, 1))
a1_2 = set_of_sums_less_than_n(10000000, b_squares, b_squares, (1, 2))
a1_3 = set_of_sums_less_than_n(10000000, b_squares, b_squares, (1, 3))
a1_7 = set_of_sums_less_than_n(10000000, b_squares, b_squares, (1, 7))


final = set()
for item in a1_7:
    if all([item in a1_3, item in a1_2, item in a1_1]):
        final.add(item)

print(len(final))