from random import random

def random_draw(distribution):
  total = 0
  cumlitive_dis = []
  for value in distribution:
    total += value
    cumlitive_dis.append(total)
  random_val = random()
  previous_val = 0
  for index in range(len(cumlitive_dis)):
    if random_val< cumlitive_dis[index]:
      return index
def find_average(distribution):
  samples = []
  for i in range(1000):
    samples.append(random_draw(distribution))
  average = 0
  for sample in samples:
    average += sample
  average = average/1000
  return average
print(random_draw([.5,.5]))
print(random_draw([.25,.25,.5]))
print(random_draw([.05,.2,.15,.3,.1,.2]))

print(find_average([.5,.5]))
print(find_average([.25,.25,.5]))
print(find_average([.05,.2,.15,.3,.1,.2]))