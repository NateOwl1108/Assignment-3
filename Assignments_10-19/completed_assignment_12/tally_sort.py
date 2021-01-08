def tally_sort(num_list):
  minimum = 999999
  for number in num_list:
    if number < minimum:
      minimum = number
  for index in range(len(num_list)):
    num_list[index] -= minimum
  tally_list = [0 for _ in range(len(num_list))]
  for number in num_list:
    tally_list[number] += 1
  sort_list = []
  for index in range(len(tally_list)):
    for instances in range(tally_list[index]):
      sort_list.append(index + minimum)
  return sort_list
print('testing tally_sort')
print(tally_sort([2, 5, 2, 3, 8, 6, 3]))
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8]
print('passed')
