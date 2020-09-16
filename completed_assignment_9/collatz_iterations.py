def collatz_iterations(number):
  iterations = 0
  while number != 1:
    if number % 2 == 0:
      number = number / 2
      iterations += 1
    else:
      number = 3 * number + 1
      iterations += 1
  return iterations

print('testing collatz_iterations(13)')
print(collatz_iterations(13))
assert collatz_iterations(13) == 9
print('Passed')

largest_iterations = 0
most_iterations_number = 0
current_number = 0
import matplotlib.pyplot as plt
plt.style.use('bmh')
number_coords = []
iterations_coords = []
for number in range(1,1000):
  current_number = number
  iterations = 0
  number_coords.append(number)
  
  while number != 1:
    if number % 2 == 0:
      number = number / 2
      iterations += 1
    else:
      number = 3 * number + 1
      iterations += 1
  iterations_coords.append(iterations)
  if iterations > largest_iterations:
    largest_iterations = iterations
    most_iterations_number = current_number

print('Number with most iterations was')
print(most_iterations_number)
plt.plot(number_coords, iterations_coords)
plt.xlabel('Numbers')
plt.ylabel('Iterations')
plt.title('Plot of iterations')
plt.savefig('plot.png')