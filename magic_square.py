def is_valid(arr):
  #rows
  for row in arr:
    row_sum =0
    for value in row:
      if value == None:
        row_sum = 15
        break
      else:
        row_sum += value
    if row_sum != 15:
      return False
  #columns
  for column in range(len(arr[0])):
    column_sum = 0
    for row in range(len(arr)):
      if arr[row][column] == None:
        column_sum = 15
        break
      else:
        column_sum += arr[row][column]
    if row_sum != 15:
      return False
  #diagnols
  diagnol_1 = 0
  for i in range(len(arr)):
    if arr[i][i] == None:
      diagnol_1 = 15
      break
    else:
      diagnol_1 += arr[i][i]

  if diagnol_1 != 15:
    return False
  
  diagnol_2 = 0
  for i in range(len(arr)):
    if arr[i][len(arr) - i -1] == None:
      diagnol_2 = 15
      break
    else:
      diagnol_2 += arr[i][i]

  if diagnol_1 != 15:
    return False

  
  return True
  

    
arr1 = [[1,2,None],
           [None,3,None],
           [None,None,None]]
print(is_valid(arr1))
True  

arr2 = [[1,2,None],
           [None,3,None],
           [None,None,4]] 
print(is_valid(arr2))
False  

arr3 = [[1,2,None],
           [None,3,None],
           [5,6,4]] 
print(is_valid(arr3))
False 
arr4 = [[None,None,None],
           [None,3,None],
           [5,6,4]] 
print(is_valid(arr4))
True   