import math

def f(x):
  return x**2 + 2*x + 1

def gradient_descent(f,x_0,alpha,δ,iterations):
  f_prime_initial = (f(x_0 + .5 * δ) - f(x_0 - .5 * δ)) / δ
  alpha_times_f_prime = alpha * f_prime_initial
  x_n = x_0 - alpha * f_prime_initial
  while iterations > 0:
    f_prime = (f(x_n + .5 * δ) - f(x_n - .5 * δ)) / δ
    x_n= x_n - alpha * f_prime
    iterations -= 1
  return x_n

print(gradient_descent(f,0,0.01,0.0001,10000))

def f(x):
  return (x**2 + math.cos(x))/(2.71828**math.sin(x))

def gradient_descent(f,x_0,alpha,δ,iterations):
  f_prime_initial = (f(x_0 + .5 * δ) - f(x_0 - .5 * δ)) / δ
  alpha_times_f_prime = alpha * f_prime_initial
  x_n = x_0 - alpha * f_prime_initial
  while iterations > 0:
    f_prime = (f(x_n + .5 * δ) - f(x_n - .5 * δ)) / δ
    x_n= x_n - alpha * f_prime
    iterations -= 1
  return x_n

print(gradient_descent(f,0,0.01,0.0001,10000))
