
def remove_parenthesis(edges):
  edges_list = []
  for index in range(len(edges)):
    edge = []
    for char in edges[index]:
      if char != '(' or char != ')':
        edge.append(char)
    edges_list.append(edge)
  return edges_list

def get_children(value, edges_list):
  edges_list = list(remove_parenthesis(edges_list))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][0] == value:
      edges.append(edges_list[index][1])
  return(edges)

def get_parents(value, edges): 
  edges_list = list(remove_parenthesis(edges))
  edges = []
  for index in range(len(edges_list)):
    if edges_list[index][1] == value:
      edges.append(edges_list[index][0])
  return(edges)

def get_root(edges):
  edges_list = list(remove_parenthesis(edges))
  parents = []
  for index in range(len(edges_list)):
    parents.append(edges_list[index][0])
  for char in parents:
    if get_parents(char, edges) == []:
      return [char]

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]
print(get_children('e', edges))
assert get_children('e', edges)==[ 'g', 'i','a'] # note: the order here doesn't matter -- you can have the
                # children in any order

assert get_children('c', edges)==[]

assert get_children('f', edges)==['h']

assert get_parents('e', edges)==[]

assert get_parents('c', edges)==['a']

assert get_parents('f', edges)==['d']

print(get_root(edges))
assert get_root(edges)==['e']