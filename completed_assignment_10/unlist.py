def unlist_nonrecursive(x):
  is_not_a_list = True
  while is_not_a_list == True:
    for value in x:
      if type(value) is list:
        x = x
      else:
        is_not_a_list = False
        return x
    x = x[0]
  
print('testing unlist_nonrecursive')
print(unlist_nonrecursive([[[[1], [2,3], 4]]]))
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], 'Answer was supposed to be [[1], [2,3], 4]'
print('Passed')

print(unlist_nonrecursive([[[[1]]]]))
assert unlist_nonrecursive([[[[1]]]]) == [1], 'Answer was supposed to be [1]'
print('Passed')

def unlist_recursive(x):
  for value in x:
    if type(value) is list:
      x = x
    else:
      is_not_a_list = False
      return x    
  return unlist_recursive(x[0])

print('testing unlist_recursive')
print(unlist_recursive([[[[1], [2,3], 4]]]))
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4], "Answer was supposed to be [[1], [2,3], 4]"

print('Passed')

print(unlist_recursive([[[[1]]]]))
assert unlist_recursive([[[[1]]]]) == [1], 'Answer was supposed to be [1]'
print('Passed')