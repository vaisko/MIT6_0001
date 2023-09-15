import string

secret_word = 'burek'

letters_guessed = ['b','r','l','f','u','k','e']


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
    //   \                   
   ||     ||
   ||     ||
   ||     || 
     \___//
      ---
    ''')

def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if not char in letters_guessed:
            return(False)
    return(True)


def get_guessed_word(secret_word, letters_guessed):
    guess = ''
    for char in secret_word:
        if not char in letters_guessed:
            guess += '_ '
        else:
            guess += str(char) + ' '
    return(guess)


def get_available_letters(letters_guessed):
    available_letters = ''
    for char in string.ascii_lowercase:
        if not char in letters_guessed:
            available_letters += char
    return(available_letters)


print(is_word_guessed(secret_word, letters_guessed))
# print(get_guessed_word(secret_word, letters_guessed))
# print(get_available_letters(letters_guessed))