#!python

patterns = ["uis", "lus", "lys"]

results = []

FILE_NAME = "wordlist.txt"
NAME = "LUIS"

def luisize(word):
  word = word.lower()
  new_word = word
  for pat in patterns:
    new_word = new_word.replace(pat, NAME)
  if new_word != word:
    return new_word

def main():

  global results

  with open(FILE_NAME, "r") as f:
    results = [luisize(line) for line in f if luisize(line)]

if __name__ == "__main__":
  main()