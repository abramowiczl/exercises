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

def decompress(input, num=1):
    print(f'input is {input}')
    num = input.split('[')[0]
    left_count = 0
    new_input_start = 0
    right_count = 0
    new_input_end = len(input)
    for i in range(len(input)):
        if input[i] == '[':
            left_count = left_count + 1
            if left_count == 1:
                new_input_start = i + 1
        if input[i] == ']':
            right_count = right_count + 1
        if left_count > 0 and left_count == right_count:
            new_input_end = i
    inner = input[new_input_start:new_input_end]
    print(f'Inner is: {inner}')
    if new_input_end == len(input):
        return int(num) * str(inner)
    else:
        return decompress(inner, num)

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