# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "Assignment2\words.txt"


def loadWords():
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


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0 # Count method takes a single arguent, element whose count is to be found. Starting at 0 letters. 
    for i, c in enumerate(secretWord): #enumerate is a built-in function of Python. It allos us to loop over something and have an automatic counter.
    # Starting a loop to check if the guessed letter is inside the secretWord. "i" is the index, and "c" is the vlaue. 
        if c in lettersGuessed:#Another loop to check if the letter is correct. "c" (value) which is a letter in "lettersGuessed"  
                count += 1 #You add a number if there is a letter in the lettersguessed that is in the secretWord. This will force the loop to start over until the amount of letters in the secretWord. 
        if count == len(secretWord): #Once the loop is done. If the amount of counts equal the amount of letters in the secretWord 
            return True #Then you return True because the word was guessed correctly.
        else: #if that does not happen 
            return False #Then you return false because the the person is missing letters to make the correct guess. 

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
#You start off with count = 0, a is the first value, a is in lettersGuessed
#so the count becomes 1, then the next letter is p, the count becomes 2, and again p, the count becomes 
#3, and then l, since there is no "l" in lettersGuessed, the count remains 3, then the next letter,  "e"
#the count becomes 4. One the secretWord letters are done, you move onto if the count equals the secretWord count of letters
#then you get True. However, the count in this case is 4 and the secretWord has 5 letters, so the output is false. 

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    count = 0 # Count method takes a single arguent, element whose count is to be found. Starting at 0 letters. 
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
    


# # When you've completed your function getGuessedWord, uncomment these three lines
# # and run this file to test!

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

# # Expected output:
# # '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def removeDupsBetter(L1, L2):
        L1Start = L1[:]
        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return removeDupsBetter(lettersGuessed, alphabet2)
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.



# # When you've completed your function getAvailableLetters, uncomment these two lines
# # and run this file to test!

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

# # Expected output:
# # abcdfghjlmnoqtuvwxyz


# def hangman(secretWord):
#     '''
#     secretWord: string, the secret word to guess.
#     Starts up an interactive game of Hangman.
#     * At the start of the game, let the user know how many 
#       letters the secretWord contains.
#     * Ask the user to supply one guess (i.e. letter) per round.
#     * The user should receive feedback immediately after each guess 
#       about whether their guess appears in the computers word.
#     * After each round, you should also display to the user the 
#       partially guessed word so far, as well as letters that the 
#       user has not yet guessed.
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE...


# # When you've completed your hangman function, uncomment these two lines
# # and run this file to test! (hint: you might want to pick your own
# # secretWord while you're testing)

# # secretWord = chooseWord(wordlist).lower()
# # hangman(secretWord)