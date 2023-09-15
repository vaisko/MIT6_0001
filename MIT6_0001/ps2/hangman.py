# Problem Set 2, hangman.py
# Name: CEO of vaisko.com
# Collaborators: n/a
# Time spent: pa ono, solidno, al cak ne previse

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2/words.txt"


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


def intro():
  print('''
      |/|       WELCOME
      | |               TO
      |/|                   ...
      | |       
      |/|       
     (___)      ▒█░▒█ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ 
     (___)      ▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ 
     (___)      ▒█░▒█ ▒█░▒█ ▒█░░▀█ ▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▒█░░▀█
     (___)      software by vaisko
     (___)                       noose by Evan M Corcoran (?)
     // \ 
    //   \                   rules:
   ||     ||                    > You have 6 guesses
   ||     ||                    > Input only lowercase letters
   ||     ||                    > ONE LETTER AT A TIME
     \___//                     > Good luck...
      ---
    ''')


def win(secret_word, score):
  print('''
              +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
              |G|R|E|A|T| |S|U|C|C|E|S|S|!|
              +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
        
        The secret word is {}  You win!!!

                  Your score : {}

        '''.format(secret_word.upper(), score)
        )


def lose(secret_word):
  print("No more guesses... You LOSE!\nThe secret word was -~{}~-".format(secret_word.upper()))
  # print('''
  #   You have FAILED 
  #         and will be DEPORTED to A̸̫̖̅͋̈́̈́ů̴͓̲͓̾s̵͈̱̰̏͆͋̚t̷͍͈̙̦̄̾͒̎r̶̼͝ą̷̛̣̋l̷̜̫̆̍̏î̸̫͜ą̶̩͎͂̀̔


  #                   _,__        .:                      
  #     The secret  <*  /        | \                     
  #              .-./     |.     :  :,                    
  #             /           '-._/     \_                  
  #            /                '       \                 
  #          .'                         *: word       
  #       .-'                             ;               
  #       |                               |               
  #       \                              /                
  #        |                            /                  
  #  was    \*        __.--._          /                  
  #          \     _.'       \:.       |                  
  #          >__,-'             \_/*_.-'                  
  #                                {}           
  #                               :--,                    
  #                                '/                     


  #                                     Have a good one!!
  #   '''.format(secret_word.upper())
  #   )


def unique_letters(word):
  letters = []
  for char in word:
     if char not in letters:
        letters.append(char)
  return letters


def is_consonant(guess):
  vowels = ('a','e','i','o','u')
  if guess in vowels:
    return False
  return True


def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
  letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
  '''
  for char in secret_word:
      if not char in letters_guessed:
          return False
  return True


def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''
  guess = ''
  for char in secret_word:
      if not char in letters_guessed:
          guess += '_ '
      else:
          guess += str(char) + ' '
  return guess


def get_available_letters(letters_guessed):
  '''
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
  '''
  available_letters = ''
  for char in string.ascii_lowercase:
      if not char in letters_guessed:
          available_letters += char
  return available_letters
  

def deduct_warning(warning_no, guess_no):
    '''
    warning_no: int, remaining warnings
    guess_no: int, remaining guesses
    reurns: tuple with modified ints
    '''
    if warning_no > 0:
      warning_no -= 1
      print('You have {} warnings left.'.format(warning_no))
    else:
      print('You have no warnings left! You just lost a guess.')
      guess_no -= 1
    
    return(warning_no, guess_no)


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
    guess_no = 6
    warning_no = 3
    letters_guessed = []
    
    print('The word is',len(secret_word),'letters long..............')
    
    while guess_no > 0:
      print('You have {} guesses left.'.format(guess_no))
      print('Available letters:',get_available_letters(letters_guessed))
      guess = input('Please guess a letter:')

      ## Checks if input is alphabetic
      if not str.isalpha(guess):
        print('\nNOT A LETTER!!!!')
        (warning_no, guess_no)=deduct_warning(warning_no, guess_no)

      ## Checks if letter is already inputed
      elif guess.lower() in letters_guessed:
        print('\nYou have already guessed this letter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        (warning_no, guess_no)=deduct_warning(warning_no, guess_no)

      else:

        ## Checks if letter is in secret word
        if guess.lower() in secret_word:
          print('Good job!!!!!')

        else:
          print('Shame. That letter IS NOT in the word!!!')
          
          ## Checks if letter is consonant
          if is_consonant(guess.lower()):
            guess_no -= 1
          
          else:
            guess_no -= 2

        letters_guessed.append(guess.lower())
      
      ## WIN
      if is_word_guessed(secret_word, letters_guessed):
        score = guess_no * len(unique_letters(secret_word))
        win(secret_word, score)
        return
      
      print(get_guessed_word(secret_word, letters_guessed))
      print('____\n')

    ## LOSE
    lose(secret_word)



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

    my_word = my_word.replace(' ', '')
    
    if len(my_word) != len(other_word):
       return False
    
    i = 0

    for char in other_word:
      if not my_word[i] == char: #or my_word[i] == '_':
        if my_word[i] == '_':
          if char in unique_letters(my_word):
              return False
        else:
           return False
      i+=1
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
       if match_with_gaps(my_word, word):
          matches.append(word)
          print(word)

    if not matches:
       print('No matches found.')


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
    guess_no = 6
    warning_no = 3
    letters_guessed = []
    
    print('The word is',len(secret_word),'letters long..............')
    
    while guess_no > 0:
      print('You have {} guesses left.'.format(guess_no))
      print('Available letters:',get_available_letters(letters_guessed))
      guess = input('Please guess a letter:')

      ## Checks if hint request
      if guess == '*':
         show_possible_matches(get_guessed_word(secret_word, letters_guessed))

      ## Checks if input is alphabetic
      elif not str.isalpha(guess):
        print('\nNOT A LETTER!!!!')
        (warning_no, guess_no)=deduct_warning(warning_no, guess_no)

      ## Checks if letter is already inputed
      elif guess.lower() in letters_guessed:
        print('\nYou have already guessed this letter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        (warning_no, guess_no)=deduct_warning(warning_no, guess_no)

      else:
        ## Checks if letter is in secret word
        if guess.lower() in secret_word:
          print('Good job!!!!!')

        else:
          print('Shame. That letter IS NOT in the word!!!')
          
          ## Checks if letter is consonant
          if is_consonant(guess.lower()):
            guess_no -= 1
          
          else:
            guess_no -= 2

        letters_guessed.append(guess.lower())
      
      ## WIN
      if is_word_guessed(secret_word, letters_guessed):
        score = guess_no * len(unique_letters(secret_word))
        win(secret_word, score)
        return
      
      print(get_guessed_word(secret_word, letters_guessed))
      print('____\n')

    ## LOSE
    lose(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # intro()
    # secret_word = 'burek'
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # print(show_possible_matches('bu___'))

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

