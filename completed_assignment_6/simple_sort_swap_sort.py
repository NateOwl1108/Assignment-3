def minimum(number_list):
    lowest_number = number_list[0]
    for number in number_list:
      if(number < lowest_number):
        lowest_number = number
    return lowest_number


print(minimum([5,8,2,2,4,3,0,2,-5,3.14,2]))
assert minimum([5,8,2,2,4,3,0,2,-5,3.14,2]) == -5, 'Answer was supposed to be -5'
print('Passed')


def simple_sort(num_list):
  sorted_elements = []
  while len(num_list) > 0:
    sorted_elements.append(minimum(num_list))
    num_list.remove(minimum(num_list))
  return sorted_elements


print(simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8], 'Answer was supposed to be [-5,0,2,2,2,2,3,3.14,4,5,8]'
print('Passed')


def swap_sort(num_list):
  swap_list = num_list
  while swap_list != simple_sort(num_list):
  
    for i in range(len(swap_list) - 1):
      if(swap_list[i] < swap_list[i - 1]):
        before_swap=swap_list[i - 1]
        swap_list[i-1] = swap_list[i]
        swap_list[i] = before_swap 
      print(swap_list)
  return(swap_list)
print(swap_sort([-5,0,2,2,2,2,3,3.14,4,5,8]))


