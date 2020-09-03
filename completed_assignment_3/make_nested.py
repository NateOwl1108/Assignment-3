def make_nested(color):
  nested_dict={}
  for key in color:
    Split=key
    catagory=Split.split('_')
    if catagory[0] in nested_dict:
      x=0
    else:  
      nested_dict[catagory[0]]={}
    sub_catagory = catagory[1]
    sub_catagory_color = color.get(key) 
    nested_dict[catagory[0]][sub_catagory]=sub_catagory_color
  return nested_dict
print('testing make_nested')
print(make_nested({
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  })=={
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
})
assert make_nested({
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  })=={
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
},'Failed.Answer should have been {}'.format({
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
})

print('Passed')
  

