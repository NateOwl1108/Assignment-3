class Node():
  def __init__(self, data):
    self.data = data
    self.next = None

A = Node(4)
print(A.data)
print(A.next)

B = Node(8)
A.next = B
print(A.next.data)

class LinkedList():
  
  def __init__(self, head):
    self.head = head
    self.data = Node(head)
    
  def print_data(self):
    print(self.data)

  def length(self):
    return len(self.data)
  
  def append(self, value):
    self.next.data = value
    self.next = value


linked_list = LinkedList(4)
print(linked_list.head.data)
4
linked_list.append(8)
print(linked_list.head.next.data)
8
linked_list.append(9)
print(linked_list.print_data())
4
8
9
print(linked_list.length())
3
