"""
Given an unordered list of three integers, write a function to check if they can form a valid date.

E.g. (2000, 14, 3) => valid
(2000, 3, 2000) => invalid
(2000, 12, 12) => valid

"""


def verify(year, month, day):
    year_valid = False
    month_valid = False
    day_valid = False
    if year > 0:
        year_valid = True
    if 0 < month < 13:
        month_valid = True
    if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day < 32:
        day_valid = True
    if month in [4, 6, 9, 11] and 0 < day < 31:
        day_valid = True
    if month == 2:
        if is_leap_year(year) and 0 < day < 30:
            day_valid = True
        if not is_leap_year(year) and 0 < day < 29:
            day_valid = True

    return year_valid and month_valid and day_valid


def is_date(date):
    comb1 = verify(date[0], date[1], date[2])
    comb2 = verify(date[0], date[2], date[1])
    comb3 = verify(date[2], date[1], date[0])
    comb4 = verify(date[2], date[0], date[1])
    comb5 = verify(date[1], date[0], date[2])
    comb6 = verify(date[1], date[2], date[0])

    return True if any([comb1, comb2, comb3, comb4, comb5, comb6]) else False


def is_leap_year(first):
    if first % 4 == 0 and first % 100 != 0:
        return True
    elif first % 400 == 0:
        return True
    else:
        return False


def test(input_param, expected):
    result = is_date(input_param)
    if result == expected:
        print(f'SUCCESS for input: {input_param}')
    else:
        print(f'FAIL for input: {input_param}')


test((2020, 11, 2), True)
test((2020, 50, 1), False)
test((2020, 30, 1), True)
test((2020, 29, 2), True)
test((2021, 29, 2), False)
test((2020, 30, 2), False)
test((1, 30, 1), True)
test((4, 45, 1), True)
