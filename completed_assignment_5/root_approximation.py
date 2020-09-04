def update_bounds(bounds):
  
  midpoint=(bounds[0]+bounds[1])/2

  if midpoint**2 > 2:
    bounds[1] = midpoint
  
  else:
    bounds[0] = midpoint
  
  return bounds

print(update_bounds([1, 2]))

assert update_bounds([1, 2]) == [1, 1.5], "Answer was supposed to be [1, 1.5]"

print('Passed')

print(update_bounds([1, 1.5]))

assert update_bounds([1, 1.5]) == [1.25, 1.5], "Answer was supposed to be [1.25, 1.5]"

print('Passed')

def estimate_root(precision, bounds):
  
  while(bounds[1]-bounds[0]) > precision:
    bounds = update_bounds(bounds)
    print(bounds)
  
  return bounds

assert estimate_root(.1, [1, 2]) == [1.375, 1.4375],    "answer was suppose to be [1.375, 1.4375]"

print('Passed')