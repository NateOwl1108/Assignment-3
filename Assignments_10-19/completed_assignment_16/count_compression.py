def count_compression(string):
  string += '~'
  previous_letter = string[0]
  compression_list = []
  consecutive_letters = 0
  for char in string:
    if previous_letter == char:
      consecutive_letters += 1
    else:
      compression_list.append((previous_letter, consecutive_letters))
      consecutive_letters = 1
    previous_letter = char
  return compression_list

print('Testing count_compression')
print(count_compression('aaabbcaaaa'))
assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)]
print('passed')

print(count_compression('22344444'))
assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)]
print('passed')
    
def count_decompression(compressed_string):
  uncompressed_string = ''
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for compressions in compressed_string:
    values = []
    for char in compressions:  
      if isinstance(char, str) == True:
        values.append(char)
      if isinstance(char, int) == True:
        values.append(char)
    while values[1] >= 1:
      uncompressed_string += values[0]
      values[1] -= 1
  return uncompressed_string

print('Testing count_decompression')
print(count_decompression([('a',3),('b',2),('c',1),('a',4)]))
assert count_decompression([('a',3),('b',2),('c',1),('a',4)]) == 'aaabbcaaaa'
print('passed')

print(count_decompression([('2',2), ('3',1), ('4',5)]))
assert count_decompression([('2',2), ('3',1), ('4',5)]) == '22344444'
print('passed')

