class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

'''A = Node(4)
print(A.data)
print(A.next)

B = Node(8)
A.next = B
print(A.next.data)'''

class LinkedList():
  
  def __init__(self, head):
    self.head = Node(head)
   
    
  def print_data(self):
    current_node = self.head
    while current_node.next != None:
      print(current_node.data)
      current_node = current_node.next

  def length(self):
    current_node = self.head
    num_nodes_visited = 1
    while current_node.next != None:
      current_node = current_node.next
      num_nodes_visited += 1
    return num_nodes_visited
  
  def append(self, value):
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = Node(value)

  def push(self, new_data):
      new_node = Node(new_data)
      new_node.next =self.head
      self.head = new_node

      current_node = self.head
      current_index = 0
      while current_node.next != None:
        current_node.index = Node(current_node)
        current_index += 1


linked_list = LinkedList(4)
print(linked_list.head.data)
4
linked_list.append(8)
print(linked_list.head.next.data)
8
linked_list.append(9)
linked_list.print_data()
4
8
9
print(linked_list.length())
3
