def even_odd_tuples(number_list):
    return [(even_odd_number, 'even') if even_odd_number % 2 == 0 else (even_odd_number, 'odd') for even_odd_number in number_list]

print('Testing even_odd_tuples for [1, 2, 3, 5, 8, 11]')
print(even_odd_tuples([1, 2, 3, 5, 8, 11]))

assert even_odd_tuples([1, 2, 3, 5, 8, 11]) == [(1, 'odd'), (2, 'even'), (3, 'odd'), (5, 'odd'), (8, 'even'), (11, 'odd')], 'Test failed. Answer was suppose to be {}'.format([(1, 'odd'), (2, 'even'), (3, 'odd'), (5, 'odd'), (8, 'even'), (11, 'odd')])
print('Passed')


def even_odd_dict(numbers):
    return {even_odd_dict_number: 'even' if even_odd_number % 2 == 0 else 'odd' for even_odd_dict_number in numbers}

print('Testing even_odd_dict for [1, 2, 3, 5, 8, 11]')
print(even_odd_dict([1, 2, 3, 5, 8, 11]))

assert even_odd_dict([1, 2, 3, 5, 8, 11]) == {
    1: 'odd',
    2: 'even',
    3: 'odd',
    5: 'odd',
    8: 'even',
    11: 'odd'
}, 'Answer was supposed to be {}'.format({
    1: 'odd',
    2: 'even',
    3: 'odd',
    5: 'odd',
    8: 'even',
    11: 'odd'
})
print('Passed')
