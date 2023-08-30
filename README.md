# Hangman 🏆
```                                
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
```
                   
Simple Hangman Game in Python. This is simple hangman game implemented in python. It has text file including all the words. Please make sure to keep all the files in one directory or else it will not work. This game selects any random word from the file and asks you to guess character for that word. You will get 6 chances to guess a word. when you guesses correct character your chance will not be counted when you gives wrong character your chance will be reduced by one.

# Game Rules 📂

The player guessing the word may, at any time, attempt to guess the whole word. If the word is correct, the game is over and the guesser wins. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. On the other hand, if the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed.

# Game character 🥷
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
   
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

  +---+
  |   |
  O   |
      |
      |
      |
=========

  +---+
  |   |
      |
      |
      |
      |
=========
```
# Using VS CODE 💻

1. Create a virtual environment. From the root directory run:
`python -m venv venv`

2. Activate the virtual environment. From the root directory run:
`source venv\scripts\activate`

3. Install required dependencies. From the root directory run:
`pip install -r requirements.txt`