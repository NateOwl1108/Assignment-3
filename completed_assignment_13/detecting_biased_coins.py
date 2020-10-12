import matplotlib.pyplot as plt
plt.style.use('bmh')

def finding_probality_for_x_heads(trials):
  had_x_heads = []
  for heads in range(len(trials[0])+1):
    had_x_heads.append(0)
    
    for results in trials:
      num_heads = 0
      
      for char in results:
        if char == 'H':
          num_heads += 1
      
      if num_heads == heads:
        had_x_heads[heads] += 1
    had_x_heads[heads] = had_x_heads[heads] / len(trials)
  
  return had_x_heads

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

plt.plot([0,1,2,3],finding_probality_for_x_heads(coin_1), linewidth = 1)
plt.plot([0,1,2,3],finding_probality_for_x_heads(coin_2), linewidth = 1)
plt.plot([0,1,2,3],finding_probality_for_x_heads(coin_3), linewidth = 1)
plt.legend(['Coin 1','Coin 2','coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Detecting Biased Coin')
plt.savefig('Biased Coin.png')

# coin 1 is slightly biased towards tails while coin three is slightly biased towards heads. Coin 2 is not biased.