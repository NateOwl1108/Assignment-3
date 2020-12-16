def merge(sorted_list_1, sorted_list_2):
    i = 0 # index in sorted_list_1
    j = 0 # index in sorted_list_2
    output_list = []
    while (i < len(sorted_list_1)) and (j < len(sorted_list_2)):
        # add another element to the output list
        list_1_entry = sorted_list_1[i]
        list_2_entry = sorted_list_2[j]
        if list_1_entry <= list_2_entry:
            output_list.append(list_1_entry)
            i += 1
        else:
            output_list.append(list_2_entry)
            j += 1
    if i == len(sorted_list_1):
     for a in range(j,len(sorted_list_2)):
        output_list.append(sorted_list_2[a])
    else:
      for b in range(i,len(sorted_list_1)):
        output_list.append(sorted_list_1[b])
    return output_list



def merge_sort(num_list):
  if len(num_list) > 1:  
    middle_index = len(num_list)//2
    first_half = num_list[:middle_index]
    second_half = num_list[middle_index:]
    print('first_half', first_half)
    print('second_half', second_half)
    first_half_sorted = merge_sort(first_half)
    second_half_sorted = merge_sort(second_half)
    print('first_half_sorted', first_half_sorted)
    print('second_half_sorted', second_half_sorted)
    return merge(first_half_sorted,second_half_sorted)
  else:
    return num_list 
print(merge_sort([4,8,7,7,4,2,3,1]))
  
  
  