import math

#A
#For the function 1+x**2+y**2 the minimum should be 1 at (0,0)

def f(x,y):
  return 1+x**2+y**2  

def gradient_descent(f,intial_point,alpha,delta,iterations):
  x_0 = intial_point[0]
  y_0 = intial_point[1]
  f_prime_initial_x = (f(x_0 + .5 * delta,y_0) - f(x_0 - .5 * delta,y_0)) / delta
  f_prime_initial_y = (f(x_0,y_0 + .5 * delta) - f(x_0,y_0 - .5 * delta)) / delta
  x_n = x_0 - alpha * f_prime_initial_x
  y_n = y_0 - alpha * f_prime_initial_y
  while iterations > 0:
    f_prime_x = (f(x_n + .5 * delta,y_n) - f(x_n - .5 * delta,y_n)) / delta
    f_prime_y = (f(x_n,y_n + .5 * delta) - f(x_n,y_n - .5 * delta)) / delta
    x_n= x_n - alpha * f_prime_x
    y_n= y_n - alpha * f_prime_y
    iterations -= 1
  return (x_n, y_n)
#B
print(gradient_descent(f,[1,2],0.01,0.0001,10000))

#C
#1+x^2+2x+y^2−9y=0
#(x+1)^2 + y^2-9y + 9/2= 9/2
#(x+1)^2 + (y-9/2)^2= 9/2
#2(x+1)^2/9 + 2(y-9/2)^2/9= 1
#the min is (-1,9/2)

def f(x,y):
  return 1 + x**2 + 2*x + y**2 + 9*-y 

def gradient_descent(f,intial_point,alpha,delta,iterations):
  x_0 = intial_point[0]
  y_0 = intial_point[1]
  f_prime_initial_x = (f(x_0 + .5 * delta,y_0) - f(x_0 - .5 * delta,y_0)) / delta
  f_prime_initial_y = (f(x_0,y_0 + .5 * delta) - f(x_0,y_0 - .5 * delta)) / delta
  x_n = x_0 - alpha * f_prime_initial_x
  y_n = y_0 - alpha * f_prime_initial_y
  while iterations > 0:
    f_prime_x = (f(x_n + .5 * delta,y_n) - f(x_n - .5 * delta,y_n)) / delta
    f_prime_y = (f(x_n,y_n + .5 * delta) - f(x_n,y_n - .5 * delta)) / delta
    x_n= x_n - alpha * f_prime_x
    y_n= y_n - alpha * f_prime_y
    iterations -= 1
  return (x_n, y_n)
#D
print(gradient_descent(f,[0,0],0.01,0.0001,10000))

