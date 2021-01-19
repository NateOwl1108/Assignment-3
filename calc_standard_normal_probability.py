inverse_root_two_pi = 1/((2*3.14)**.5)
def function(a):
  return inverse_root_two_pi * 2.718**(-(a**2)/2)

def calc_standard_normal_probability(a,b):
  probability = 0
  while a < b:
    probability += 0.001 * function(a)
    a += 0.001
  return probability
print(calc_standard_normal_probability(-1,1))
print(calc_standard_normal_probability(-2,2))
print(calc_standard_normal_probability(-3,3))

