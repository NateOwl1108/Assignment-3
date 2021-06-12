
class HashTable():

  def __init__(self,num_buckets):
    self.num_buckets = num_buckets
    self.buckets = [[] for i in range(self.num_buckets)]
  
  def hash_function(self,string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum_string = 0
    for char in string:
      sum_string += alphabet.index(char)
    return sum_string % self.num_buckets

  def insert(self, key, value):
    index = self.hash_function(key)
    if self.buckets[index] in self.buckets:
      self.buckets[index].append((key,value))
    return self.buckets

  def find(self, key):
    index = self.hash_function(key)
    for group in self.buckets[index]:
      if key in group:
        return group[1]

ht = HashTable(num_buckets = 3)
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2    

ht.insert('cabbage', 5)
assert ht.buckets  == [[], [], [('cabbage',5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21