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
print(cartesian_product([['a'], [1,2,3], ['Y','Z']]))