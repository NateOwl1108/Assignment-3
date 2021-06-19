def bisection_search(wanted, entries):
  #get high and low indexs
  low = 0
  high = len(entries)-1

  #find midpoint
  midpoint = round((low + high)/2)
  #loop through until correct
  while entries[midpoint] != wanted:
    #if not update high or low
    if entries[midpoint]> wanted:
      high = midpoint-1

    elif entries[midpoint]< wanted:
      low = midpoint + 1
    #update midpoint
    midpoint = round((low + high)/2)
  return midpoint

assert bisection_search(21, [5, 7, 9, 20, 21, 22, 23]) == 4

#b. Suppose you have a sorted list of 16 elements. What is the greatest number of iterations of bisection search that would be needed to find the index of any particular element in the list? Justify your answer.
#4 since if wanted = 11 then  
#low = 0 high = 16 mid = 8
#low = 9 high = 16 mid = 13 
#low = 9 high = 12 mid = 11 
#low = 9 high = 10 mid = 10





  