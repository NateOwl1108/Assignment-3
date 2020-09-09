def skip_factorial_nonrecursive(n):
  factorial=1
  if(n % 2 ==0):
    while n > 1:
      factorial = factorial * n
      n -= 2
  else:
     while n > 0:
      factorial = factorial * n
      n -= 2
  return factorial

print(skip_factorial_nonrecursive(6))
assert skip_factorial_nonrecursive(6) == 48, 'Answer is supposed to be 48'
print ('passed')

print(skip_factorial_nonrecursive(7))
assert skip_factorial_nonrecursive(7) == 105, 'Answer is supposed to be 105'
print ('passed')