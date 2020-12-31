import matplotlib.pyplot as plt
plt.style.use('bmh')

def function(x):
  return 1/(1+2.71828**(-0.693*x + 2.215))

def plot_function(function ):
  plt.plot([1, 2, 3], [.2,.25,.5], 'ro') # plot red ('r') circles ('o')
  x= 0
  x_values = []
  y_values = []
  for i in range(301):
    x_values.append(x)
    y_values.append(function(x))
    x+=.01
  plt.plot(x_values,y_values)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('function ')
  plt.savefig('Assignment 33 graph')

plot_function(function)




