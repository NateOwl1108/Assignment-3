def intersection(list1,list2):
  output=[]
  for char in list_1:
    if char in list_2:
      output.append(char)
  return output
list_1=[1,2,'a','b']
list_2=[2,3,'a']
print (intersection(list_1,list_2))
assert intersection(list_1,list_2)==[2,'a'],'Answer was {} when it should have been {}'.format(intersection(list_1,list_2),[2,'a'])
print("Passed")
def union(list1,list2):
  union_set1=set(list1)
  union_set2=set(list2)
  union=union_set1.union(union_set2)
  return list(union)
list_1=[1,2,'a','b']
list_2=[2,3,'a']
print(union(list_1,list_2))
assert union(list_1,list_2)==[1,2,3,'a','b'],'Test failed. Answer was {}'.format(union(list_1,list_2))
print('passed')
    
  