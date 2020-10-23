from random import random

def probability(num_heads, num_flips):
  posibilities = 2 ** num_flips 
  flips_fact = head_fact = flip_minus_head_fact = 1

  for i in range(1,num_flips+1): 
    flips_fact = flips_fact * i 

  for i in range(1,num_heads+1): 
    head_fact = head_fact * i 

  for i in range(1,num_flips -num_heads + 1): 
    flip_minus_head_fact = flip_minus_head_fact * i 

  num_heads_outcomes = flips_fact / (head_fact * flip_minus_head_fact)
  return num_heads_outcomes / posibilities

print(probability(5,8))
assert probability(5,8) == 0.21875, 'Answer was supposed to be 0.21875'
print('Passed')


def monte_carlo_probability(num_heads, num_flips):
  
  had_num_head = 0
  was_head = 0
  for i in range(1000):
    was_head = 0
    for j in range(num_flips):
      
      rand = round(random())
      if rand == 0:
        was_head += 1
    if was_head == num_heads:
      had_num_head += 1

  return had_num_head / 1000
print(monte_carlo_probability(5,8))
print(monte_carlo_probability(5,8))
print(monte_carlo_probability(5,8))
print(monte_carlo_probability(5,8))
print(monte_carlo_probability(5,8))
