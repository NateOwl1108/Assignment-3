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
  
  probability = 0
  probability_list = [[],[]]

  if rule == "left endpoint":
    for index in range(len(n)-1):
      step_size = (b-a)/n[index]
      print('')
      probability = 0
      while a < b:
        probability += step_size * function(a)
        a += step_size
      probability_list[1].append(probability)
      probability_list[0].append(n[index])
    return probability_list

  elif rule == "right endpoint":
    for index in range(len(n)-1):
      step_size = (b-a)/n[index]
      probability = 0
      while a < b-step_size:
        a += step_size
        probability += step_size * function(a)
      probability_list[1].append(probability)
      probability_list[0].append(n[index])
    return probability_list

  elif rule =="midpoint":
    for index in range(len(n)-1):
      step_size = (b-a)/n[index]
      probability = 0
      while a < b-step_size:
        probability += step_size * function((a+a+ step_size)/2)
        a += step_size
      probability_list[1].append(probability)
      probability_list[0].append(n[index])
    return probability_list

  #if rule is trapezoidal
  elif rule == "trapezoidal":
    for index in range(1, len(n)-1):
      step_size = (b-a)/n[index]
      probability = (b-a)/n[0]*0.5 * function(a)
      while a < b-step_size:
        a += step_size
        probability += step_size * function(a)
      probability += step_size *0.5* function(a+step_size)
      probability_list[1].append(probability)
      probability_list[0].append(n[index])
      print('probability trapezoidal',probability)
    return probability_list

    #If rule is Simpson
  elif rule == "simpson":
    for index in range(len(n)-1):
      step_size = (b-a)/n[index]
      probability = (b-a)/n[0]*1/3 * function(a)
      ocilator = -1
      while a < b-step_size:
        a += step_size
        ocilator = ocilator *-1
        probability += (3+ocilator) * step_size * function(a)
      probability += step_size *1/3* function(a+step_size)
      probability_list[1].append(probability)
      probability_list[0].append(n[index])
    return probability_list

n = [ n*2 for n in range(1,50)]
left = calc_standard_normal_probability(0,1,n,"left endpoint")
'''right = calc_standard_normal_probability(0,1,n,"right endpoint")
mid = calc_standard_normal_probability(0,1,n,"midpoint")
trap =calc_standard_normal_probability(0,1,n,"trapezoidal")
simpson = calc_standard_normal_probability(0,1,n,"simpson")'''
plt.plot(left[0],left[1],label = "left")
'''plt.plot(right[0],right[1], label = 'right')
plt.plot(mid[0],mid[1], label= "midpoint")
plt.plot(trap[0],trap[1], label = "trapezoidal")
plt.plot(simpson[0],simpson[1], label = "simpson")'''
plt.legend() 
plt.savefig('calc_standard_normal_probability')




  

