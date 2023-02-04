"""
In this exercise, you're going to decompress a compressed string.
Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input
3[abc]4[ab]c

Would be output as
abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
Characters allowed as input include digits, small English letters and brackets [ ].
Digits are only to represent amount of repetitions.
Letters are just letters.
Brackets are only part of syntax of writing repeated substring.
Input is always valid, so no need to check its validity.
"""


def decompress(input):
    # print(f'input is {input}')
    left_count = 0
    new_input_start = 0
    right_count = 0
    new_input_end = len(input)
    num = 1
    for i in range(len(input)):
        if input[i] == '[':
            left_count = left_count + 1
            if left_count == 1:
                new_input_start = i + 1
                j = 1
                num = 0
                while input[i-j].isnumeric():
                    num = num + int(input[i-j])*10**(j-1)
                    j = j + 1

        if input[i] == ']':
            right_count = right_count + 1
        if left_count > 0 and left_count == right_count:
            new_input_end = i
            break
    num_len = len(str(num))
    before_inner = input[:new_input_start-1-num_len] if new_input_start > 0 else ''
    inner = input[new_input_start:new_input_end]
    rest = input[new_input_end + 1:]
    # print( ' ')
    # print(f'Before inner is: {before_inner}')
    # print(f'Inner is: {inner}')
    # print(f'Rest is: {rest}')
    # print(f'Num is: {num}')
    # print(' ')
    if right_count == 0:
        return str(inner)
    else:
        return decompress(before_inner + int(num)*inner + rest)

def test(input, expected):
    print('-----------------')
    result = decompress(input)
    if expected == result:
        print(f'SUCCESS! Decompressed {input} is {result}')
    else:
        print(f'FAILED! Decompressed {input} should be {expected} but was {result}')

test('3[abc]', 'abcabcabc')
test('3[abc]4[ab]c', 'abcabcabcababababc')
test('10[a]', 'aaaaaaaaaa')
test('2[3[a]b]', 'aaabaaab')