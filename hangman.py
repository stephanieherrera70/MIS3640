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
    
    count = 0 #Count method takes a single agument, element whose count is to be found. Starting a 0 letters, and each time it is a correct letter, the count will increase.
    blank = ['_ '] * len(secretWord) #An underscore will be multiplied by how my letters in the secretWord. 

    for i, c in enumerate(secretWord):#Creaing a loop, "i" is the count and "c" is the value or letter in the secretWord.
        if c in lettersGuessed:#If letter is in lettersGuesssed 
            count += 1 #The count will increase by 1 since the letter matches a letter in secretWorld. 
            blank.insert(count-1,c)#You are inserting the letter on the line of words. The the letter will be placed in the index number. 
            blank.pop(count) #pop() removees and returns the last item in the lsit. This will remove the underscore.
            if count == len(secretWord):#Once all of the letters match the number of letter in the secretworkd
                return ''.join(str(t) for t in blank) #then return join() merges the string representations of elements in sequence "e" into a string, with seperator string. 
        else: #if the letter is not in secretWrod
            count += 1 #You add the guess as a count. 
            blank.insert(count-1,'_') #A blank will be placed in hold of the person not guessing the letter. The count-1, is for the index in the word. If the count is 4, then the placement of the letter is 3: 0,1,2,3. 
            blank.pop(count)#The pop removes the underscore that you need to get rid of because it created an extra index.
            if count == len(secretWord):#Once the guessed letters match up to the amount of letter for secretWord you are done with the loop.
                return ''.join(str(t) for t in blank) #this brings it all together. 

# # When you've completed your function getGuessedWord, uncomment these three lines
# # and run this file to test!

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
#So, you start off with "a", it jumps to the else statement. It counts 1, and inserts a "_" for the first letter of the 
#list of "_" because it is index 0. Then "p", count becomes 2 and will go with the first part of the function. It will add a 
#"p" in the 1st index, and pop out a blank because a letter was inserted. You do this for every letter. 

# # Expected output:
# # '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
     
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']# Every letter in the alphebet. 
    alphabet2 = alphabet[:] #Copy of the alphetbet. There will be letters being removed on this list to show what letters have not been used. Constantly referring back to the first alphebet. 

    def removeduplicate(L1, L2): #This is a function that has 2 arguments. 
        L1Start = L1[:]# Have to make sure to make a copy of the first list, to be able to modify the second.
        for e in L1:#For an element, or letter in the first argument.
            if e in L1Start:#If the leter in LIStart is there, which also implies it is in the first argument
                L2.remove(e) #then the letter is removed from the second argyment.
        return ''.join(str(e) for e in L2)

    return removeduplicate(lettersGuessed, alphabet2) #This will sshow what letters are available. 

    #Alphabet2 becomes L2. So the letter starts off from the alphabet and as each letter is guessed, it is removed from
    #the list and then all the letters left are displayed. 

    #  Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.



# # When you've completed your function getAvailableLetters, uncomment these two lines
# # and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# # Expected output:
# # abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    intro = str(len(secretWord)) #This allows the computer to know how long the secretWord is. 
    lettersGuessed = [] #This shows all the letters that have been guessed and will be places in here. 
    guess = str #turns the guess into a string and makes sure it is a string. 
    mistakesMade = 8 #This is how many attempts the player had. Every time they guess, the number will decrease by 1. 
    wordGuessed = False #
    
    print('Welcome to the game, Hangman!')
    print(('I am thinking of a word that is ') + intro + (' letters long.'))
    print('------------')
    #These are the instructions for the game. 
    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False: #Making sure the guesses are within the limit of guessing. You can only get up to 8 guesses for this one.
        if secretWord == getGuessedWord(secretWord, lettersGuessed):#If the secretWord is equal to the actual word through this function 
            wordGuessed = True #then the wordGuessed is True and you are done. 
            break
        print(('You have ') + str(mistakesMade) + (' guesses left.'))
        print(('Available letters: ') + getAvailableLetters(lettersGuessed))
        #This tells the players how many guesses they have by inserting the number of how many guesses are left.
        guess = input(('Please guess a letter: ').lower()) #this allows the user to guess a letter and make it into a lowercase just incase. 
        if guess in secretWord: #If the guess is in the secretWord it would move to the next two if statements. 
            if guess in lettersGuessed: #If letter has already been guessed
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)) 
                print(('------------'))
            else:
                lettersGuessed.append(guess) #You would add the guessed letter into the guess []. 
                print(('Good guess: ') + getGuessedWord(secretWord, lettersGuessed))
                print(('------------'))
        else: #If the guess is not in the secretWord it would move to the next if else statements. 
            if guess in lettersGuessed: #If letter has already been guessed
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print(('------------'))
            else: #If the guess is not in the secret word, the user will have one less guess. 
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print(('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed))
                print(('------------'))

    if wordGuessed == True: #If the wordGuessed is equal to the secretWord, the game will tell the user that they won. 
        return 'Congratulations, you won!'
    elif mistakesMade == 0: #If user has guessed incorrectly 8 times, and there are no more guesses left, the game will tell you that they lost and give you the secretWord. 
        print(('Sorry, you ran out of guesses. The word was ') + secretWord)



# # When you've completed your hangman function, uncomment these two lines
# # and run this file to test! (hint: you might want to pick your own
# # secretWord while you're testing)

secretWord = chooseWord(wordlist).lower() #This will generate a secret word. 
print(hangman(secretWord)) #This will call upon the hangman function, randomized secretWrod, and start the game. 