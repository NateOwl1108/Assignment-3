#a_(n)=3*a_(n-1)-4
#a_1=5
def first_n_terms(n):
  term_list=[5]
  last_term=0
  next_term=0
  for i in range(n-1):
    last_term=term_list[-1]
    next_term=3*last_term-4
    term_list.append(next_term)
  return term_list

print('testing first_n_terms for input 10')
print(first_n_terms(10))
assert first_n_terms(10)==[5,11,29,83,245,731,2189,6563,19685,59051],'Test failed. Answer was {}'.format(nth_term(10))
print('Passed')
def nth_term(n):
  if n==1 or n==0:
    return 5
  return 3*nth_term(n-1)-4
print ('testing nth_term for input 10')
print(nth_term(10))
assert nth_term(10)==59051,'Test failed. Answer was {}'.format(nth_term(10))
print("passed")