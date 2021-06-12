

def hash_function(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum_string = 0
    for char in string:
      sum_string += alphabet.index(char)
    return sum_string

def insert(array_input, key, value):
    index = hash_function(key)
    if array_input[index] in array_input:
      array_input[index].append((key,value))
    return array_input

def find(input_array, key):
    index = hash_function(key)
    for group in intput_array[index]:
      if key in group:
        return group[1]

print(array)
array = [[], [], [], [], []]

insert(array, 'a', [0,1])
insert(array, 'b', 'abcd')
insert(array, 'c', 3.14)
print(array)
[[('a',[0,1])], [('b','abcd')], [('c',3.14)], [], []]

insert(array, 'd', 0)
insert(array, 'e', 0)
insert(array, 'f', 0)
print(array)
[[('a',[0,1]), ('f',0)], [('b','abcd')], [('c',3.14)], [('d',0)], [('e',0)]]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
