def count_characters(string):
  alphabet='abcdefghijklmnopqrstuvwxyz !?.'
  count={}
  lowercase=list(string.lower())
  for char in alphabet:
    letter=0
    lower=(string.lower())
    if char in string:
      letter=char.lower()
      count[letter]=lower.count(letter)
  return count
print('Testing count_characters for input A cat!!!')
print(count_characters('A cat!!!'))
assert count_characters('A cat!!!')=={'a':2,'c':1,'t':1,' ':1, '!': 3},'test failed. Answer was {}'.format(count_characters('A cat!!!'))
print ('Passed')
