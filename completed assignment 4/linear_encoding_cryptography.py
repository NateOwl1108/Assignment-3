import math


def encode(string, a, b):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    encoded_list = []

    for char in string:

        if char in string:

            letter_number = alphabet.index(char)

            encoded_list.append(a*letter_number + b)

    return encoded_list

print('Testing encode for input [a cat, 2, 3]')

print(encode('a cat', 2, 3))

assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], 'Answer was supposed to be {}'.format([5, 3, 9, 5, 43])

print("Passed")


def decode(encription, a, b):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    decripted_string = ''

    test_encription = []

    for char in encription:

        test_encription.append((char - b) / a)

    for char in test_encription:

        if round(char) != char or char < 0 or char > 26:

            return False
        decripted_string += alphabet[round(char)]

    return decripted_string

print('Testing decode for input ([5, 3, 9, 5, 43], 2, 3)')

print(decode([5, 3, 9, 5, 43], 2, 3))

assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', 'Answer was supposed to be {}'.format('a cat')

print('Passed')

print('Testing decode for input ([1, 3, 9, 5, 43], 2, 3)')

print(decode([1, 3, 9, 5, 43], 2, 3))

assert decode([1, 3, 9, 5, 43], 2, 3) is False, 'Answer was supposed to be {}'.format(False)

print('Passed')


def decode_all(encription):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    decripted_string_list = []

    string_true = True

    test_encription = []

    for a in range(100):

        for b in range(100):

            decripted_string = ''

            string_true = True

            test_encription = []

            for char in encription:

                test_encription.append((char - b) / (a+1))

            for unecrypted_num in test_encription:

                if round(unecrypted_num) != unecrypted_num or unecrypted_num < 0 or unecrypted_num > 26:

                    string_true = False

                else:

                    decripted_string += alphabet[round(unecrypted_num)]

            if string_true is True:

                decripted_string_list.append(decripted_string)

    return decripted_string_list

print(decode_all([377,
 717,
 71,
 513,
 105,
 921,
 581,
 547,
 547,
 105,
 377,
 717,
 241,
 71,
 105,
 547,
 71,
 377,
 547,
 717,
 751,
 683,
 785,
 513,
 241,
 547,
 751]))
