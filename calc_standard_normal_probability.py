import matplotlib.pyplot as plt
plt.style.use('bmh')
def function(a):
  inverse_root_two_pi = 1/((2*3.14)**.5)
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

def calc_standard_normal_probability(a,b,n,rule):
  step_size = (b-a)/n
  probability = 0
  probability_list = [[],[]]
  if rule == "left endpoint":
    while a < b - step_size:
      probability += step_size * function(a)
      probability_list[1].append(probability)
      probability_list[0].append(a)
      a += step_size
    return probability_list
  elif rule == "right endpoint":
    while a < b:
      a += step_size
      probability += step_size * function(a)
      probability_list[1].append(probability)
      probability_list[0].append(a)
    return probability_list
  elif rule =="midpoint":
    next_x = a + step_size
    while a < b:
      probability += step_size * function((a+next_x)/2)
      probability_list[1].append(probability)
      probability_list[0].append(a)
      a += step_size
      next_x += step_size
    return probability_list
  elif rule == "trapezoidal":
    probability += step_size*.5*function(a)
    probability_list[1].append(probability)
    probability_list[0].append(a)
    while a < b:
      a += step_size
      probability += step_size * function(a)
      probability_list[1].append(probability)
      probability_list[0].append(a)
    a += step_size
    probability += step_size * .5 * function(a)
    probability_list[1].append(probability)
    probability_list[0].append(a)
    return probability_list
  elif rule == "simpson":
    probability += step_size*1/3*function(a)
    probability_list[1].append(probability)
    probability_list[0].append(a)
    osolator = 1
    while a < b:
      a += step_size
      probability += (3+osolator)*step_size * function(a)
      probability_list[1].append(probability)
      probability_list[0].append(a)
      osolator = osolator * -1
    a += step_size
    probability += step_size * 1/3 * function(a)
    probability_list[1].append(probability)
    probability_list[0].append(a)
    return probability_list
left = calc_standard_normal_probability(0,1,50,"left endpoint")
right = calc_standard_normal_probability(0,1,50,"right endpoint")
mid = calc_standard_normal_probability(0,1,50,"midpoint")
trap =calc_standard_normal_probability(0,1,50,"trapezoidal")
simpson = calc_standard_normal_probability(0,1,50,"simpson")
plt.plot(left[0],left[1],label = "left")
plt.plot(right[0],right[1], label = 'right')
plt.plot(mid[0],mid[1])
plt.plot(trap[0],trap[1])
plt.plot(simpson[0],simpson[1])
plt.savefig('calc_standard_normal_probability')




  

