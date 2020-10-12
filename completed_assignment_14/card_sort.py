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

print(card_sort([12, 11, 13, 5, 6]))
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
print('passed')

print(card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]))
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7]
print('Passed')