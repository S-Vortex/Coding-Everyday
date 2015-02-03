# Import necessary modules
import sys
import random

# Set messages
welcome = 'Hello, We await your defense of the accused'
rules = 'Rules:\nTo play, type a letter and press Enter\
\nGuessing incorrectly will increase your limb count by 1 and your incorrect\
\nentry will be added to a word bank for you to see. Typing a letter a second\
\ntime will result in another failure. Correctly guessing the word/phrase\
\nbefore you reach full limb count will grant you victory and you will save\
\nthe accused man.'

#Get random word and other values
#  - Functions are at bottom of code
correctWord = getword()
limbcount = random.randint(4, 9)
finished = false
currentLimbCount = 0
incorrectLetters = ''
currentBoard = ''
# - makes currentBoard the same length as the correct word
for i in range(0, len(correctWord)):
  currentBoard = currentBoard + '-'


#Main game loop
while



# Gets a random word from the small wordbank
def getword():
  wordbank = ['study', 'orchard', 'flavorful', 'dragon', 'watercolor', 'Russian', 'tea', 'sports', 'process', 'sleep', 'long', 'list', 'of', 'boring', 'words', 'that', 'never', 'should', 'exist']
  return wordbank[random.randint(0, len(wordbank))]
