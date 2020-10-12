import math

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

def kl_divergence(p, q):
  divergence = 0
  for index in range(len(p)):
    if (p[index] != 0) and (q[index] != 0) :
      divergence += p[index] * math.log((p[index] / q[index])) / math.log(2.718281828459045)
  divergence = round(divergence * (10**11)) / 10**11
  return divergence

def card_sort(num_list):
  sorted_list = []
  for num in num_list:
    if len(sorted_list) == 0:
      sorted_list.append(num)
    else:
      for index in range(len(sorted_list)):
        if num <= sorted_list[index]:
          sorted_list.insert(index, num)
          break
        if index + 1 == len(sorted_list):
          sorted_list.append(num)
          break
  return sorted_list


def approximations_of_randomness(flips):
  flips_values = []
  name_order = []
  for key in flips:
    flips_values.append(flips[key])
    name_order.append(key)

  splits = []
  for index in range(len(flips_values)):
    splits.append(flips_values[index].split())

  probabilities = []
  for index in range(len(flips_values)):
    probabilities.append(finding_probality_for_x_heads(splits[index]))

  divergence = []
  for index in range(len(flips_values)):
    divergence.append(kl_divergence(probabilities[index], [.0625, .25, .375, .25, .0625]))
  index = 0
  
  for key in flips:
    flips[key] = divergence[index]
    index += 1

  sorted_list = card_sort(divergence)

  for key in flips:
    if flips[key] == sorted_list[0]:
      print(key)
  return sorted_list
  


flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}

print(approximations_of_randomness(flips))