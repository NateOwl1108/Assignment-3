def minimum(number_list):
    lowest_number = number_list[0]
    for number in number_list:
        if(number < lowest_number):
            lowest_number = number
    return lowest_number

print('Testing minimum')
print(minimum([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]))
assert minimum([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == -5, 'Answer was supposed to be -5'
print('Passed')


def simple_sort(num_list):
    sorted_elements = []
    while len(num_list) > 0:
        sorted_elements.append(minimum(num_list))
        num_list.remove(minimum(num_list))
    return sorted_elements

print('testing simple_sort')
print(simple_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]))
assert simple_sort([5, 8, 2, 2, 4, 3, 0, 2, -5, 3.14, 2]) == [-5, 0, 2, 2, 2, 2, 3, 3.14, 4, 5, 8], 'Answer was supposed to be [-5,0,2,2,2,2,3,3.14,4,5,8]'
print('Passed')


def swap_sort(num_list):
    all_swapped_check = True
    loop_check = False
    while(all_swapped_check < ):
      all_swapped_check = 0

      for i in range(len(num_list)-1):
        
        if(num_list[i] < num_list[i - 1]):
          num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
          all_swapped_check = False
      if all_swapped_check == True:

       


      
    return num_list

print(swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))

#coundn't solve this last one


