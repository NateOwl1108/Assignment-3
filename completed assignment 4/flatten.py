def flatten(color_dictionary):

    flat_dictionary = {}

    for key in color_dictionary:

        catagory = key

        sub_catagory = color_dictionary.get(key)

        for key in sub_catagory:
            flat_dictionary[catagory+'_'+key] = sub_catagory.get(key)

    return flat_dictionary

colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

print('Testing flatten for input:')

print(colors)

print("")

print('Flatten of input was:')

print(flatten(colors))

assert flatten(colors) == {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}, 'Test Failed. Answer was supposed to be {} but was {}.'.format(colors, flatten(colors))

print("Passed")
