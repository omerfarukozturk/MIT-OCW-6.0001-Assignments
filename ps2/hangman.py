# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ''
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word += letter
      else:
        guessed_word += '_ '
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ''

    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        available_letters += letter
        
    return available_letters 
    
def play_hangman(secret_word, special_char = None):
  
  print('Welcome to the game Hangman!')
  print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')

  remaining_guess_count = 6
  remaining_invalid_guess_count = 3
  letters_guessed = []
  valid_guessed_letters = []

  print('You have '+ str(remaining_invalid_guess_count) + ' warnings left.')

  while remaining_guess_count > 0:
    print('-------------')
    print('You have ' + str(remaining_guess_count) + ' guesses left.')
    print('Available letters: ' + get_available_letters(letters_guessed))
    guess = input('Please guess a letter: ').lower()
    
    guessed_word = get_guessed_word(secret_word,letters_guessed)
    
    # allow for the case where the user can guess an asterisk (*), in which case the computer will print out all the words that match that guess.
    if special_char == '*' and guess == '*':
      print('Possible word matches are:')
      show_possible_matches(guessed_word)
      continue

    # If the user inputs anything besides an alphabet (symbols, numbers)..
    if not (guess.isalpha() and len(guess) == 1):
      remaining_invalid_guess_count -= 1
      if remaining_invalid_guess_count >= 0:
        print('Oops! That is not a valid letter. You have '+ str(remaining_invalid_guess_count) + ' warnings left: ' + guessed_word)
      else:
        # If the user has no warnings, they should lose one guess
        remaining_guess_count -= 1   
      continue     

    # If the user inputs a letter that has already been guessed..
    if guess in letters_guessed:
      remaining_invalid_guess_count -= 1
      if remaining_invalid_guess_count >= 0:
        print('Oops! You''ve already guessed that letter. You have '+ str(remaining_invalid_guess_count) + ' warnings left: ' + guessed_word)
      else:
        # If the user has no warnings, they should lose one guess.
        remaining_guess_count -= 1 
        
        print('Oops! You''ve already guessed that letter. You have no warnings left so you lose one guess: ' + guessed_word)  
      continue
    else:
      letters_guessed.append(guess)

    if guess in secret_word:      
      guessed_word = get_guessed_word(secret_word,letters_guessed)
      valid_guessed_letters.append(guess)
      print('Good guess: ' + guessed_word)

      if guessed_word == secret_word:
        print('-------------')
        print('Congratulations, you won!')
        score = remaining_guess_count * len(valid_guessed_letters)
        print('Your total score for this game is: ' + str(score))
        return
    else:
      print('Oops! That letter is not in my word: ' + guessed_word)

      # If the vowel hasn’t been guessed and the vowel is not in the secret word, the user loses ​two​ guesses.
      # If the user inputs a consonant that hasn’t been guessed and the consonant is not in the secret word, the user loses ​one​ guess.
      remaining_guess_count -= 2 if guess in 'aeiou' else 1

  print('-----------')
  print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    play_hangman(secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ','')

    if len(my_word) != len(other_word):
      return False

    for i in range(len(my_word)):
      char = my_word[i]
      if char == '_':
        continue

      if char == other_word[i]:
        if len(my_word.replace(char, '')) != len(other_word.replace(char, '')):
          return False      
      else:
        return False

    return True if len(my_word) == len(other_word) else False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = []

    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches.append(word)
  
    print(' '.join(matches) if len(matches) != 0 else 'No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    play_hangman(secret_word, special_char='*')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
