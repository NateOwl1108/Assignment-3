class Stack():
  def _init_(list,value):
  list=[]
  def push(value):
    list.append(value)
  def pop(value):
    list.pop()
  def peek():
    print(list[len(list) -1])
  def data():
    print(list)

s = Stack()
s.data
s.push('a')
s.push('b')
s.push('c')
s.data

s.pop()
s.data

s.peek()

s.data


