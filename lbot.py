#!python
results = []

patterns = ["uis", "lus", "lys"]
FILE_NAME = "wordlist.txt"
NAME = "LUIS"

#Check if the word is luizable.
#If yes, luize it 
def luisize(word):
    word = word.lower()
  new_word = word
  for pat in patterns:
      new_word = new_word.replace(pat, NAME)
  if new_word != word:
      return new_word

def getLuisWord():

  global results
  
  with open(FILE_NAME, "r") as f:
    results = [luisize(line) for line in f if luisize(line)]

  #debugging purposes
  return resullts[0]

