import random as r
vocab = ["Blue,"Red","Green","Yellow"]
definitions = {
  "Blue": "A color",
  "Red": "Another color"
  "Green": "A third color"
  "Yellow": "A fourth color"
}

def word_study():
  ran = r.randint(0,len(vocab)
  word = vocab[ran)
  input("What does "+word+"mean? "]
  print(word+"means"+definitions[word])
word_study()


