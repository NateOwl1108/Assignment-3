def f(x):
  return x**3 + x - 1

def estimate_derivative(f,c,δ):
  
  return (f(c + .5 * δ) - f(c - .5 * δ)) / δ

def zero_of_tangent_line(f, c, δ):
  f_c = f(c)
  slope = estimate_derivative(f, c, δ)
  zero_of_tangent_line = (-(f_c) / slope) + c
  return zero_of_tangent_line

def estimate_solution(f, initial_guess, δ, precision):
  previous_guess = 0
  guess = zero_of_tangent_line(f, initial_guess, δ)
  while abs(previous_guess - guess) > precision:
    previous_guess = guess
    guess = zero_of_tangent_line(f, previous_guess, δ)
  return guess

print('testing zero_of_tangent_line')    
answer = zero_of_tangent_line(f, 0.5, 0.001)
print(round(answer,6))
assert round(answer,6) == 0.714286
print('passed')

print('testing estimate_solution')
answer = estimate_solution(f, 0.5, 0.001, 0.01)
print(round(answer, 6))
assert round(answer,6) == 0.682328
print('passed')