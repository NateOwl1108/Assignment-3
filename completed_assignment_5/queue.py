class Queue():
  
  def __init__(self):
    self.data=[]

  def enqueue(self,value):
    self.data.append(value)

  def dequeue(self):
    self.data.pop(0)

  def peek(self):
    return self.data[0]

q = Queue()
q.data
assert(q.data) == []

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.data)
#assert q.data == ['a', 'b', 'c']

q.dequeue()
print(q.data)
assert q.data == ['b', 'c']

q.peek()
assert q.peek() == 'b'

print(q.data)
assert q.data == ['b', 'c']
