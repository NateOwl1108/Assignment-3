class Stack:
     def __init__(self):
         self.full_data = []

     def push(self, value):
         self.full_data.append(value)

     def pop(self):
         return self.full_data.pop()

     def peek(self):
         return self.full_data[len(self.full_data)-1]

     def data(self):
        return (self.full_data)



s = Stack()
print('testing for Stack')
assert s.data()==[],'Answer was {} when it should have been {}'.format(s.data(),[])
print(s.data())
print('Passed')
 
s.push('a')
s.push('b')
s.push('c')
print('testing for Push')
assert s.data()==['a','b','c'],'Answer was {} when it should have been {}'.format(s.data(),['a','b','c'])
print(s.data())
print('Passed')
s.pop()

print('testing for Pop')
assert s.data()==['a','b'],'Answer was {} when it should have been {}'.format(s.data(),['a','b'])
print(s.data())
print('Passed')

print('testing for Peek')
assert s.peek()=='b','Answer was {} when it should have been {}'.format(s.peek(),'b')
print(s.peek())
print('Passed')

print('testing for Data')
assert s.data()==['a','b'],'Answer was {} when it should have been {}'.format(s.data(),[])
print(s.data())
print('Passed')


