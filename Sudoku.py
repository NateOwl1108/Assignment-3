

def check_if_in_box(arr, row, col, value):
    left = True
    if row%2!=0:
      row = row -1
    if col >= len(arr)/2:
      left = False
    box = []
    for row_index in range(row, row+2):
      row = arr[row_index]
      if left == False:
        box.append(row[round(len(arr)/2):])
      else:
        box.append(row[:round(len(arr)/2)])
    
    for row_value in box:
      if value in row_value:
        return False
    return True

def is_valid(arr, row , column, value):
  #rows
  if value in arr[row]:

    return False
    
  #columns
  if value in [arr[col_row][column] for col_row in range(len(arr))]:

    return False

  if check_if_in_box(arr,row,column, value) == False:

    return False
  return True

def move_back(non_changable_positions, arr, position):
  #if position at start of row move to end of previous row
  if position[1] == 0:
        position[0] -= 1
        position[1] = len(arr) -1
  else:
  #move back 1
    position[1] -= 1
  #while the position is in non_changable_positions continue moving back
  while position in non_changable_positions:
    if position[1] == 0:
        position[0] += 1
        position[1] = len(arr) -1
    else:
      position[1] -= 1
  return position

def move_foward(non_changable_positions, arr, position):
  if position[1] == len(arr)-1:
        position[0] += 1
        position[1] = 0
  else:
  #move back 1
    position[1] += 1
  #while the position is in non_changable_positions continue moving back
  while position in non_changable_positions:
    if position[1] == 5:
        position[0] += 1
        position[1] = 0
    else:
      position[1] += 1
  return(position)

def sudoku(non_changable_positions, arr):
  length = len(arr)
  position = [0, 0]
  loop_over = False
  while True:
    start_value = 0
    no_value = True
    
    #check if value exists at position
    if arr[position[0]][position[1]] != 0:
      start_value = arr[position[0]][position[1]]

    #go through values at position 
    for value in range(start_value+1, length+1):
      #check if valid
      if is_valid(arr, position[0], position[1], value) == False:

          continue
      else:
      #if valid stop increasing value
        if position[0] == 5 and position[1] == 5:
          loop_over = True
        arr[position[0]][position[1]] = value
        no_value = False
        break

    #if final value works return arr
    if loop_over == True:
      return arr
      break
    else:
      #if no values work move back until valid position
      if no_value == True:
          arr[position[0]][position[1]] = 0
          position = move_back(non_changable_positions, arr, position)
      #else move foward until valid position
      else:
        position = move_foward(non_changable_positions, arr, position)
    

def print_sudoku(arr):
  for row_index in range(len(arr)):
    if row_index%2 == 0:
      print('---------------------')
    row_string = '|'
    for column_index in range(len(arr)):
      if column_index == round(len(arr)/2):
        row_string += '|'
      row_string += " " + str(arr[row_index][column_index]) + " "
    row_string += '|'
    print(row_string)
  print('---------------------')

    
        
  


#create array
arr = [[0 for _ in range(6)] for _ in range(6)]
arr[0][2] = 4
arr[1][3] = 2
arr[1][4] = 3
arr[2][0] = 3
arr[2][4] = 6
arr[3][1] = 6
arr[3][5] = 2
arr[4][1] = 2
arr[4][2] = 1
arr[5][3] = 5

for row in arr:
  print(row)
print('')

non_changable_positions = [[0,2],[1,3],[1,4],[2,0],
[2,4],[3,1],[3,5],[4,1],[4,2],[5,3]]

arr = sudoku(non_changable_positions,arr)
print_sudoku(arr)

  

  


