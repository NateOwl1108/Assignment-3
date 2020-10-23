import math

def f(x):
  return x**2 + 2*x + 1

def gradient_descent(f,x_0,alpha,δ,iterations):
  f_prime_initial = (f(x_0 + .5 * δ) - f(x_0 - .5 * δ)) / δ
  print
  x_n = 0
  x_n_= x_0 - alpha * f_prime_initial
  while iterations > 0:
    f_prime = (f(x_n + .5 * δ) - f(x_n - .5 * δ)) / δ
    x_n -= alpha * f_prime_initial
    iterations -= 1
  return x_n

print(gradient_descent(f,0,0.01,0.0001,10000))

def f(x):
  return (x**2 + math.cos(x))/math.sin(x)

def gradient_descent(f,x_0,alpha,δ,iterations):
  f_prime_initial = (f(x_0 + .5 * δ) - f(x_0 - .5 * δ)) / δ
  x_n = 0
  x_n_= x_0 - alpha * f_prime_initial
  while iterations > 0:
    f_prime = (f(x_n + .5 * δ) - f(x_n - .5 * δ)) / δ
    x_n -= alpha * f_prime_initial
    iterations -= 1
  return x_n

print(gradient_descent(f,0,0.01,0.0001,10000))
