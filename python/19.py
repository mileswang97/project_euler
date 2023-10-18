# looks annoying af

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from typing import Tuple

Months = {
    1: 3,
    2: 0,
    3: 3,
    4: 2,
    5: 3,
    6: 2,
    7: 3,
    8: 3,
    9: 2,
    10: 3,
    11: 2,
    12: 3,
}


def months_in_year(
    year_number: int,
    first_day: int,
    is_leap_year: bool = False,
) -> Tuple[list, int]:
    first_of_the_month = 13 * [
        0,
    ]  # last entry is next year jan
    first_of_the_month[0] = first_day

    for i in range(1, 13):
        first_of_the_month[i] = (first_of_the_month[i - 1] + Months[i]) % 7

    return first_of_the_month[0:12], first_of_the_month[12]


print(months_in_year(year_number=1900, first_day=1, is_leap_year=False))


def main(start_year=1901, end_year=2000):
    main_array = list()
