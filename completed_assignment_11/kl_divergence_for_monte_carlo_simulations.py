import math
from random import random

def kl_divergence(p, q):
  divergence = 0
  for index in range(len(p)):
    if (p[index] != 0) and (q[index] != 0) :
      divergence += p[index] * math.log((p[index] / q[index])) / math.log(2.718281828459045)
  divergence = round(divergence * (10**11)) / 10**11
  return divergence

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]
print('testing kl_divergence ...')
print(kl_divergence(p,q))
assert kl_divergence(p,q) == -0.09637237851 
print('passed')

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

def monte_carlo_probability(num_heads, num_flips, samples):
  had_num_head = 0
  was_head = 0
  for i in range(samples):
    was_head = 0
    for j in range(num_flips):
      
      rand = round(random())
      if rand == 0:
        was_head += 1
    if was_head == num_heads:
      had_num_head += 1
  return had_num_head / samples

def lists_of_probabilities(flips,samples):
  true_probabilities = []
  monte_carlo_probabilities = []
  for head in range (flips + 1):
    true_probabilities.append(probability(head,8))
    monte_carlo_probabilities.append(monte_carlo_probability(head,8,samples))
  return [true_probabilities , monte_carlo_probabilities ]

print('kl_divergence for 1000 samples')
p = lists_of_probabilities(8,1000)[0]
q = lists_of_probabilities(8,1000)[1]
print(kl_divergence(p,q))
print('kl_divergence for 100 samples')
p = lists_of_probabilities(8,100)[0]
q = lists_of_probabilities(8,100)[1]
print(kl_divergence(p,q))
print('kl_divergence for 10,000 samples')
p = lists_of_probabilities(8,10000)[0]
q = lists_of_probabilities(8,10000)[1]
print(kl_divergence(p,q))
# As the number of samples increases, the KL divergence approaches 0 because with standard deviation, a larger sample size will allow for a more accurate average that will get closer to the true probability .