class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class DoublyLinkedList():
  
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
    current_node.next.prev = current_node

  def push(self, new_data):
      new_node = Node(new_data)
      new_node.next =self.head
      self.head = new_node

      current_node = self.head
      current_index = 0
      while current_node.next != None:
        current_node.index = Node(current_node)
        current_index += 1

  def get_node(self, index):

      current_node = self.head
      current_index = 0
      while current_index != index:
        current_node = current_node.next
        current_index += 1
      return current_node
  
  def insert(self, new_data, index):
      current_node = self.head
      current_index = 0
      while current_index != index:
        current_node = current_node.next
        current_index += 1
      new_node = Node(new_data)
      new_node.next = current_node

      current_node = new_node
      current_index = index
      while current_node.next != None:
        current_node.index = Node(current_node)
        current_index += 1

  def delete(self, index):
      current_node = self.head
      current_index = 0
      while current_index != index:
        current_node = current_node.next
        current_index += 1
      while current_node.next.next != None:
        current_node = current_node.next


doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)


current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
    current_node = current_node.prev
    node_values.append(current_node.data)
assert node_values == ['e', 'c', 'b', 'a']