c = 0
for i in range(68,9999):
  c += 1/i**4
print(c)
c= 1/c
print(c)



value = 68
total = c/value**4
print(total)
while total <= .95:
  value += 1
  total += c/value**4
  
print(value)