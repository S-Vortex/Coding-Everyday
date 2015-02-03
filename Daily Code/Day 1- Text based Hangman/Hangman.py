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

wordbank = ['study', 'orchard', 'flavorful', 'dragon', 'watercolor', 'Russian', 'tea', 'sports', 'process', 'sleep', 'long', 'list', 'of', 'boring', 'words', 'that', 'never', 'should', 'exist']
correctWord = wordbank[random.randint(0, len(wordbank))]
currentLimbCount = 0
limbcount = random.randint(4, 9)
ended = False
incorrectLetters = ''
currentBoard = ''
changed = False
failed = False
tempString = ''
# - makes currentBoard the same length as the correct word
for i in range(0, len(correctWord)):
  currentBoard = currentBoard + '-'



def screen():
  print 'Currently in rope: ' + str(currentLimbCount) + '/' + str(limbcount) + 'limbs'
  print 'Letters used: ' + incorrectLetters
  print 'Current board: ' + currentBoard

def checkInput():
  changed = False
  for i in range(len(correctWord)):
    if guess == correctWord[i]:
      for i in range(0, len(correctWord)):
        if j == i:
          tempString = currentBoard + guess
        else:
          tempString = tempString + currentBoard[j]
      changed = True
  if changed == False:
    print 'Incorrect Input'
    currentLimbCount += 1
    incorrectLetters = incorrectLetters + character + ', '

def otherStuff():
  if currentBoard == correctWord:
    solved = True
    ended = True
  if currentLimbCount == limbCount:
    failed = False
    ended = True

#Get random word and other values
#  - Functions are at bottom of code


print rules
#Main game loop
while ended == False:
  screen()
  guess = raw_input('Enter a letter: ')
  checkInput()
  otherstuff()
