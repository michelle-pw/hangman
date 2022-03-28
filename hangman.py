import random
from hangmanwords import words
import string

# list has words that contain "-" or " ", which cannot be used in hangman. This randomly chooses a word that does not contain "-" or " "
def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_word(words)
  # to store letters in the word
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  # to store what the user has guessed
  used_letters = set()

  lives = 8

  # to get user input and making them uppercase
  while len(word_letters) > 0 and lives > 0:
    # letters used
    # ' '.join(['a','b','cd']) --> 'a b cd'
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    # what current word is (ie W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)

      else:
        # takes away lives if wrong word
        lives = lives - 1
        print('Letter is not in word.')

    elif user_letter in used_letters:
      print('You have already guessed that character, please try another one:')

    else:
      print('Invalid character, please try again.')

    # gets here when len(word_letters) == 0 or when lives == 0
  if lives == 0:
    print('You have no more lives left, sorry! The word was', word)
  else:
    print('You guessed the word', word, '!')

hangman()
