def parse_value(string):
  if string[0] == '"' and string[-1] == '"':
    return string.strip('"')
  elif '.' in string:
    return float(string)
  else:
    return int(string)

test_string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
coma_seperated_values = [x.split(',') for x in test_string.split('\n')]

arr = []

for value_list in coma_seperated_values:
  parsed_values = [parse_value(element) for element in value_list]
  arr.append(parsed_values)

print(arr)
