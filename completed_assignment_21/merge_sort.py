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
x = None
z = 5*x
x = 5

y = z
print(y)

print(merge([-2,1,4,4,4,5,7],[-1,6,6]))
assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7]
print('passed')