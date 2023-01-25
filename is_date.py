"""
Given an unordered list of three integers, write a function to check if they can form a valid date.

E.g. (2000, 14, 3) => valid
(2000, 3, 2000) => invalid
(2000, 12, 12) => valid

"""

def verify(first, second, third):
    first_valid = False
    second_valid = False
    third_valid = False
    if first > 0:
        first_valid = True
    if second > 0 and second < 13:
        second_valid = True
    if second in [1, 3, 5, 7, 8, 10, 12] and third > 0 and third < 32:
        third_valid = True
    if second in [4, 6, 9, 11] and third > 0 and third < 31:
        third_valid = True
    if second == 2:
        if is_leap_first(first) and third > 0 and third < 30:
            third_valid = True
        if not is_leap_first(first) and third > 0 and third < 29:
            third_valid = True

    return first_valid and second_valid and third_valid


def is_date(obj):
    comb1 = verify(obj[0], obj[1], obj[2])
    comb2 = verify(obj[0], obj[2], obj[1])
    comb3 = verify(obj[2], obj[1], obj[0])
    comb4 = verify(obj[2], obj[0], obj[1])
    comb5 = verify(obj[1], obj[0], obj[2])
    comb6 = verify(obj[1], obj[2], obj[0])

    if any([comb1, comb2, comb3, comb4, comb5, comb6]):
        return True
    else:
        return False


def is_leap_first(first):
    if first % 4 == 0 and first % 100 != 0:
        return True
    if first % 400 == 0:
        return True
    else:
        return False


def test(obj, expected):
    result = is_date(obj)
    if (result == expected):
        print(f'SUCCESS for obj: {obj}')
    else:
        print(f'FAIL for obj: {obj}')


test((2020, 11, 2), True)
test((2020, 50, 1), False)
test((2020, 30, 1), True)
test((2020, 29, 2), True)
test((2021, 29, 2), False)
test((2020, 30, 2), False)
test((1, 30, 1), True)
test((4, 45, 1), True)