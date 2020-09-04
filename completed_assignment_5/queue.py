class Queue():

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        self.data.pop(0)

    def peek(self):
        return self.data[0]

q = Queue()
print('testing for init')
print(q.data)
assert(q.data) == [], "answer should have been {}".format([])
print('passed')

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print('testing for enqueue')
print(q.data)
assert q.data == ['a', 'b', 'c'], "answer should have been {}".format(['a', 'b', 'c'])
print('Passed')

q.dequeue()
print('testing for dequeue')
print(q.data)
assert q.data == ['b', 'c'], "answer should have been {}".format(['b', 'c'])
print('passed')

print('testing for peek')
q.peek()
assert q.peek() == 'b', "answer should have been 'b'"
print('passed')

print('testing for data')
print(q.data)
assert q.data == ['b', 'c'], "answer should have been {}".format(['b', 'c'])
print('passed')
