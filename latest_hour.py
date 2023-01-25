"""
Latest Hour

Given a time (in 24-hour format) with missing digits marked as '?',
we want to replace all of the question marks by digits (0-9) in such a way as to
obtain the latest possible time.
The earliest possible time is 00:00 and the latest valid time is 23:59.

Write a function:

class Solution { public String solution(String T); }

that, given a string T, returns the latest valid time that can be obtained from T,
as a string in the format "HH:MM", where HH denotes a two-digit value for hours and
MM denotes a two-digit value for minutes.

Examples:

1. Given T = "2?:?8", the function should return "23:58".

2. Given T = "?8:4?", the function should return "18:49".

3. Given T = "??:??", the function should return "23:59".

4. Given T = "06:34", the function should return "06:34".

Assume that:

T consists of exactly five characters; the third one is ':'; the others are digits (0-9) or '?';
there always exists a valid time obtained by substituting '?' with digits.

"""


def latest_hour(time):
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    new_hour = replace_hour(hour)
    new_minute = replace_minute(minute)
    return new_hour + ':' + new_minute


def replace_hour(hour):
    first = hour[0]
    second = hour[1]

    if first in ['?', '2'] and second == '?':
        return '23'
    if first == '?' and second in ['0', '1', '2', '3']:
        return '2' + second
    if first == '?' and second in ['4', '5', '6', '7', '8', '9']:
        return '1' + second
    if first in ['0', '1'] and second == '?':
        return first + '9'
    else:
        return hour


def replace_minute(minute):
    first = minute[0]
    second = minute[1]

    if first == '?':
        first = '5'
    if second == '?':
        second = '9'
    return first + second


def test(time, expected):
    result = latest_hour(time)
    if expected == result:
        print(f'SUCCESS! {result}')
    else:
        print(f'FAILED! Should be {expected} but was {result}')


test('2?:?8', '23:58')
test('?8:4?', '18:49')
test('??:??', '23:59')
