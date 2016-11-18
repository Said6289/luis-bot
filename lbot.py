#!python

patterns = ["uis", "lus", "lys"]

FILE_NAME = "wordlist.txt"
NAME = "LUIS"

def luisize(word):
  words = []
  for pat in patterns:
    new_word = word.replace(pat, NAME)
    if new_word != word:
      words.append(new_word)
  return words

def main():
  with open(FILE_NAME, "r") as f:
    results = [line for line in f for substr in patterns if substr in line]

  for r in results:
    for a in luisize(r):
      print(a)

if __name__ == "__main__":
  main()