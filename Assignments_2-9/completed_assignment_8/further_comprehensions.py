def identity_matrix_elements(n):
  #1 line of code
  return [[( 1 if x == y else 0) for x in range(n)] for y in range(n)]

print('testing for identity_matrix_elements')
print(identity_matrix_elements(4))
assert identity_matrix_elements(4) == [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
print('Passed')


def counting_across_rows_matrix_elements(m,n):
  return [[(n*y + x + 1) for x in range(n)] for y in range(m)] 

print('testing counting_across_rows_matrix_elements')
print(counting_across_rows_matrix_elements(3,4))
assert counting_across_rows_matrix_elements(3,4) ==[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print('passed')

