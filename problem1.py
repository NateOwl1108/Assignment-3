import math
def convert_to_base_10(n):
  num_string=str(n)
  length=len(num_string)
  value=0
  while (length>0):
    exponent=2**(length-1)
    value+=(math.floor(n/(10**(length-1))))*exponent
    n-=round(n/(10**(length-1)))*(10**(length-1))
    length-=1
    
  return value
print('testing for convert to base 10 of input 10011')
assert convert_to_base_10(10011)==19,'output was {} when it should have been {}'.format(convert_to_base_10(10011),19)
print(convert_to_base_10(10011))
