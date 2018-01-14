# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess=''
    for i in secretWord:
        if i in lettersGuessed:
            guess+=i
        else:
            guess+='_ '
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    total,choices=string.ascii_lowercase,''
    for i in total:
        if i not in lettersGuessed:
            choices+=i
    return choices







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
    # FILL IN YOUR CODE HERE...
    lettersGuessed,choices,guessedword='','',''
    print('The length of the word is '+str(len(secretWord))+' letters')
    print('----------------------------------------------------------')
    num_guess=8
    game_over=False
    while num_guess>0 and game_over==False:
        print('you have '+str(num_guess)+' guesses remaining')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess=raw_input('Guess a letter:')
        guess=guess.lower()
        if guess in lettersGuessed:
            print('Letter already guessed.'+getGuessedWord(secretWord,lettersGuessed))
            continue
        else:
            lettersGuessed+=guess
        if guess in secretWord:
            print('Good Guess: '+ getGuessedWord(secretWord,lettersGuessed))
            game_over=isWordGuessed(secretWord,lettersGuessed)
        else:
            print('guessed letter not in the word '+getGuessedWord(secretWord,lettersGuessed))
            num_guess-=1
        print('----------------------------------------------')
    if game_over==True:
        print('Congratulations, You won!')
    else:
        print('Game over, You lost! The word was :'+str(secretWord))




    # When you've completed your hangman function, uncomment these two lines
    # and run this file to test! (hint: you might want to pick your own
    # secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
