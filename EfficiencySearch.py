#Author: Sujay Kandwal sfk5645@psu.edu
import re
import time

def avoids(word, letters):
  for c in letters:
    if c in word:
      return False
  return True

def get_words_from_text(filename):
  words = []
  with open(filename) as fin:
    for line in fin:
      line_words = re.split("[^0-9a-zA-Z']+", line)
      for word in line_words:
        if avoids(word, "0123456789"):
          word = word.lstrip("'")
          if len(word) > 0:
            words.append(word)
  return words

def load_dictionary_list(dictfilename):
  words = []
  with open(dictfilename) as dictfin:
    for line in dictfin:
      words.append(line.strip())
  return words

def get_misspelled_0(dictionary, text):
  misspelledList = []
  for word in text:
    wordToLower = word.lower()
    if wordToLower not in dictionary:
      misspelledList.append(word)
  return misspelledList

def get_misspelled_1(dictionary, text):
  misspelledList = []
  start = 0
  end = len(dictionary)-1 
  midPoint = 0 
  for word in text:
    inDictionary = False
    wordToLower = word.lower()
    while (start <= end):
      midPoint = (start+end)//2
      if dictionary[midPoint] < wordToLower:
        start = midPoint + 1
      elif dictionary[midPoint] > wordToLower:
        end = midPoint - 1
      elif dictionary[midPoint] == wordToLower:
        inDictionary = True
        start = end 
        start+= 1
    if inDictionary == False:
      misspelledList.append(word)
    start = 0
    end = len(dictionary) - 1
  return misspelledList

def get_misspelled_2(dictionary, text):
  misspelledList = []
  dictionary2 = set(dictionary)
  text2 = set()
  for word in text:
    word2 = word.lower()
    text2.add(word2)
  set3 = text2 - dictionary2
  for word in text:
    word2 = word.lower()
    if word2 in set3:
      misspelledList.append(word)
  return misspelledList

def run():
  dictname = input("Enter dictionary file name: ") 
  dictionary = load_dictionary_list(dictname)
  textname = input("Enter text file name: ")
  text = get_words_from_text(textname)
  option = int(input("Enter an option 0-2 (0:listEff1, 1:listEff2, 2:setEff1): "))
  options = [get_misspelled_0, get_misspelled_1, get_misspelled_2]
  start = time.perf_counter() 
  misspelled = options[option](dictionary, text)
  end = time.perf_counter() 
  for w in misspelled:
    print(w)
  print(f"Dictionary has {len(dictionary)} words; Text has {len(text)} words.")
  print(f"Text has {len(misspelled)} misspelled words.")
  print(f"{end-start} seconds.")

if __name__ == "__main__":
  run()