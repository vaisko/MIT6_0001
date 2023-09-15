# Problem Set 4B
# Name: vaisko
# Collaborators: vaisko.com
# Time Spent: 2:00 possibly

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("ps4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'ps4/words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict = {}

        for i in range(len(string.ascii_lowercase)):
            if i+shift > 25:
                dict.update({string.ascii_lowercase[i]:string.ascii_lowercase[i+shift-26]})
                dict.update({string.ascii_uppercase[i]:string.ascii_uppercase[i+shift-26]})
            else:
                dict.update({string.ascii_lowercase[i]:string.ascii_lowercase[i+shift]})
                dict.update({string.ascii_uppercase[i]:string.ascii_uppercase[i+shift]})

        return dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dict = self.build_shift_dict(shift)
        new_message = ''

        for char in self.message_text:
            if char not in dict:
                new_message += char
            else:
                new_message += dict.get(char)

        return new_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift = shift
        self.build_shift_dict(shift)
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.build_shift_dict(shift)
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

        return


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        dict = {}
        s = 0

        for i in range(26):
            dict.update({i:0})
            new_message = self.apply_shift(i)
            for word in new_message.split():
                if is_word(self.valid_words,word):
                    dict[i]+=1

        for i in dict:
            if dict[i] == max(dict.values()):
                s = i
        
        return (26-s,self.apply_shift(s))


if __name__ == '__main__':

    plain_msg1 = PlaintextMessage('We need to solve the crack cocaine epidemic!!!',1)
    print(f'Input: {plain_msg1.get_message_text()}')
    print('Expected output: Xf offe up tpmwf uif dsbdl dpdbjof fqjefnjd!!!')
    print(f'Actual output: {plain_msg1.get_message_text_encrypted()}', end='\n----------')  

    plain_msg2 = PlaintextMessage('Live, laugh, love',11)
    print(f'Input: {plain_msg2.get_message_text()}')
    print('Expected output: Wtgp, wlfrs, wzgp')
    print(f'Actual output: {plain_msg2.get_message_text_encrypted()}', end='\n----------')

    cipher_msg1 = CiphertextMessage('tvearw')
    print(f'Input: {cipher_msg1.get_message_text()}')
    print('Expected output: (4, \'prawns\')')
    print('Actual Output:', cipher_msg1.decrypt_message(), end='\n----------')

    cipher_msg2 = CiphertextMessage('vlcxay')
    print(f'Input: {cipher_msg2.get_message_text()}')
    print('Expected output: (20, \'bridge\')')
    print('Actual Output:', cipher_msg2.decrypt_message(), end='\n----------')

    #TODO: best shift value and unencrypted story 
    
    story = CiphertextMessage(get_story_string())
    print(f'Shift value and decrypted story:\n{story.decrypt_message()}')
