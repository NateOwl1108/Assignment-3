def zero_of_tangent_line(c):
  f_c = (c**3) + (c - 1 )
  slope = 3*(c**2) + 1
  zero_of_tangent_line = ((-f_c) / slope) + c
  return zero_of_tangent_line

print('testing zero_of_tangent_line')
answer = zero_of_tangent_line(0.5)
print(round(answer,6))
assert round(answer,6) == 0.714286
print('passed')

def estimate_solution(initial_guess, precision):
  previous_guess = 0
  guess = zero_of_tangent_line(initial_guess)
  while abs(previous_guess - guess) > precision:
    previous_guess = guess
    guess = zero_of_tangent_line(previous_guess)

  return guess

print('testing estimate_solution')
answer = estimate_solution(0.5, 0.01)
print(round(answer, 6))
assert round(answer,6) == 0.682328
print('passed')
