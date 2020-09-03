import math


def convert_to_base_2(base_10):

    binary = 0

    exponent = 0

    while base_10 > 0:

        exponent = math.floor(math.log(base_10, 2))

        binary += 10**exponent

        base_10 -= 2**exponent

    return binary

input = 19

print('testing convert_to_base_2 for input ' + str(input))

print(convert_to_base_2(input))

assert convert_to_base_2(input) == 10011, 'Test failed. Answer was supposed to be {}'.format(10011)

print('Passed')
