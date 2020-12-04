def merge(list_1, list_2):
  merged_list = []
  while (len(list_1) != 0) & (len(list_2) != 0):
    list_1_min = list_1[0]
    list_2_min = list_2[0]
    
    if list_1_min <= list_2_min:
      merged_list.append(list_1_min)
      list_1.remove(list_1_min)

    else:
      merged_list.append(list_2_min)
      list_2.remove(list_2_min)
  
    if len(list_1) == 0:
      merged_list.append(list_2_min)
      list_2.remove(list_2_min)
    if len(list_2) == 0:
      merged_list.append(list_1_min)
      list_1.remove(list_1_min)
    
  return merged_list

def merge_sort(num_list):
  length = len(a_list)
  middle_index = length//2
  first_half = a_list[:middle_index]
  second_half = a_list[middle_index:]
  sorted_list = []
  if len(first_half) > 1:
    merge_sort(first_half)
    
  if len(second_half) > 1:
    merge_sort(first_half)
  if len(second_half) == 1 and len(first_half) == 0:
    merge(first_half,second_half)

  
  return 
  
  
  