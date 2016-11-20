# This file should probably be renamed

import random

patterns = ["uis", "lus", "lys"]
FILE_NAME = "wordlist.txt"
NAME = "<i>luis</i>"

# Check if the word is luizable.
# If yes, luize it 
def luisize(word):
  new_word = word
  for pat in patterns:
      new_word = new_word.replace(pat, NAME)
  if new_word.lower() != word.lower():
      return new_word

def getLuisWord():
  results = []

  with open(FILE_NAME, "r") as f:
    results = [luisize(line) for line in f if luisize(line)]

  # For dbugging purposes
  random.seed()
  rand = random.randrange(len(results))
  return results[rand]

