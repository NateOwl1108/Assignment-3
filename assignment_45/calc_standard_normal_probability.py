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
  #if rule is left endpoint
  if rule == "left endpoint":
    step_size = (b-a)/n
    
    x = a
    num_steps = 0
    while x < b:
      num_steps +=1
      probability += step_size * function(x)
      x =a+ step_size * num_steps

    return probability

  #if rule is right endpoint
  elif rule == "right endpoint":
    step_size = (b-a)/n
    probability = 0
    x = a
    num_steps = 0
    while x < b:
      num_steps +=1
      x =a+ step_size * num_steps
      probability += step_size * function(x)
    return probability

  #if rule is midpoint
  elif rule =="midpoint":
    step_size = (b-a)/n
    probability = 0
    x = a
    num_steps = 0
    while x < b:
      num_steps += 1
      probability += step_size * function((2*x + step_size)/2)
      x =a+ step_size * num_steps
    return probability

  #if rule is trapezoidal
  elif rule == "trapezoidal":
    step_size = (b-a)/n
    x = a
    probability += step_size * 0.5* function(x)
    num_steps = 0
    while x < b-step_size:
      num_steps += 1
      x =a+ step_size * num_steps
      probability += step_size * function(x)
    probability += step_size *0.5*function(x+step_size)
    return probability

    #If rule is Simpson
  elif rule == "simpson":
    step_size = (b-a)/n
    x = a
    probability += step_size *1/3*function(x)
    num_steps = 0
    ocilator = 1
    while x < b-step_size:
      num_steps += 1
      x =a+ step_size * num_steps
      probability += (3+ocilator)*1/3 * step_size * function(x)
      ocilator = ocilator*-1
      
    probability += step_size *1/3*function(x+step_size)
    return probability
left = [[],[]]
right = [[], []]
mid = [[],[]]
trapezoidal = [[],[]]
simpson =[[],[]]
for n in range(1,51):
   left[1].append(calc_standard_normal_probability(0,1,n*2,"left endpoint"))
   left[0].append(n*2)
   right[1].append(calc_standard_normal_probability(0,1,n*2,"right endpoint"))
   right[0].append(n*2)
   mid[1].append(calc_standard_normal_probability(0,1,n*2,"midpoint"))
   mid[0].append(n*2)
   trapezoidal[1].append(calc_standard_normal_probability(0,1,n*2,"trapezoidal"))
   trapezoidal[0].append(n*2)
   simpson[1].append(calc_standard_normal_probability(0,1,n*2,"simpson"))
   simpson[0].append(n*2)


plt.plot(left[0],left[1],label = "left")
plt.plot(right[0],right[1], label = 'right')
plt.plot(mid[0],mid[1], label= "midpoint")
plt.plot(trapezoidal[0],trapezoidal[1], label = "trapezoidal")
plt.plot(simpson[0],simpson[1], label = "simpson")
plt.legend() 
plt.savefig('calc_standard_normal_probability')




  

