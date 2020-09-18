from random import random
import matplotlib.pyplot as plt
plt.style.use('bmh')
heads = [0,1,2,3,4,5,6,7,8]
true_distribution_probability = []
monte_carlo_probability_1 = []
monte_carlo_probability_2 = []
monte_carlo_probability_3 = []
monte_carlo_probability_4 = []
monte_carlo_probability_5 = []


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
for head in range (9):
  true_distribution_probability.append(probability(head,8))
  monte_carlo_probability_1.append(monte_carlo_probability(head,8))
  monte_carlo_probability_2.append(monte_carlo_probability(head,8))
  monte_carlo_probability_3.append(monte_carlo_probability(head,8))
  monte_carlo_probability_4.append(monte_carlo_probability(head,8))
  monte_carlo_probability_5.append(monte_carlo_probability(head,8))

plt.plot(heads,true_distribution_probability,linewidth = 2.5)
plt.plot(heads,monte_carlo_probability_1,linewidth = 0.75 )
plt.plot(heads,monte_carlo_probability_2,linewidth = 0.75 )
plt.plot(heads,monte_carlo_probability_3,linewidth = 0.75 )
plt.plot(heads,monte_carlo_probability_4,linewidth = 0.75 )
plt.plot(heads,monte_carlo_probability_5,linewidth = 0.75 )


plt.legend(['True','MC 1','MC 2','MC 3', 'MC 4', 'MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('plot.png')