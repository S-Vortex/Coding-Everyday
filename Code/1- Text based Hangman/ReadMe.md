Hang-Man (Text based)
===============
Author: Sam M
Site: S-Vortex.com
Date: October 26, 2014
Development Environment: Atom text editor
Language: Python 2.7
Dependencies: none
Design Document: Design Doc.html


Description: A simple game of Hangman

To run: All you need besides Python is the Hangman.py in this folder
1. Open a Command Prompt, Power-shell, Shell, or Terminal
2. Navigate to the folder where Hangman.py is located
  - For info on how to do this, Google "Navigating using cd" for your operating system
3. In your shell, type "python Hangman.py"
4. Game should start


Design:
To include: limb count, letter bank, blanks for correct guesses to fill,
   welcome message, rules, failure screen
Limits (to keep length down): No visuals outside necessary text, No screen
   refreshing (results must be inline)
Organization:
   - Main
      - Welcome
      - Rules
      - Collect Data
        - Get random word from word bank
      - Display
        - Current progress
        - Incorrect letters
        - Limb count
      - Completion
        - Failure: Limb count reached, the man has been hanged
        - Success: You have saved the Hangman!
      - Go again or quit?
