def cartesian_product(arrays):
  array_lenth = len(arrays)
  points = []
  for var in arrays[0]:
    points.append([var])
  for i in range(1, array_lenth):
    points_length = len(points)
    product = []
    for old_point in points:
      for new_data in arrays[i]:        
         new_point = list(old_point)
         new_point.append(new_data)
         product.append(new_point)
    points = product
  return points

def grid_search(two_variable_function, grid_lines):
  all_points = cartesian_product(grid_lines)
  minimum_of_function = 9999999
  smallest_coordinates = []
  for index in range(len(all_points)):
    if two_variable_function(*all_points[index]) < minimum_of_function:
      minimum_of_function = two_variable_function(*all_points[index])
      smallest_coordinates = all_points[index]
  return smallest_coordinates
def two_variable_function(x, y):
        return (x-1)**2 + (y-1)**3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]
assert grid_search(two_variable_function, grid_lines)==[0.75, 0.9]