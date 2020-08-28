def make_nested(color):
  animal=[]
  food=[]
  for key in color:
    Split=key
    print (key)
    catagory=Split.split('_')
    if(catagory[0]=='animal'):
      animal.append(catagory[1])
    if(catagory[0]=='food'):
      food.append(catagory[1])
    print(catagory)
  color={'animal':{animal[0],animal[1],animal[2]},'food':{food[0],food[1]}}
  return color
make_nested({
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
  })

