def separate_into_words(sentence):
  return sentence.split(' ')
print(separate_into_words("look the dog ran fast"))

separate_into_words("look the dog ran fast")
def reverse_word_order(sentence):
  words_list = separate_into_words(sentence)
  reverse = words_list[::-1]
  reverse_sentence = ''
  reverse_sentence += reverse[0]
  for index in range(1,len(reverse)):
    reverse_sentence += " " + reverse[index]
  print(reverse_sentence)
  return reverse_sentence
assert reverse_word_order("look the dog ran fast") == "fast ran dog the look"
