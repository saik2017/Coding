from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score=0
    score=0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word=''
    # For each word in the wordList
    for word in wordList:
        if isValidWord(word,hand,wordList):
            score=getWordScore(word,n)
            if score>max_score:
                best_word=word
                max_score=score
    if best_word=='':
        return None
    else:
        return best_word

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    len_hand=calculateHandlen(hand)
    score=0
    pts=0
    while len_hand>0:
        displayHand(hand)
        word=compChooseWord(hand,wordList,n)
        if word==None:
            break
        else:
            pts=getWordScore(word,n)
            print(" The chosen word is "+str(word)+" and it's worth "+str(pts)+' points')

            score+=pts
            hand=updateHand(hand,word)
            len_hand=calculateHandlen(hand)

    print("The total score is :"+str(score))
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    hand={}
    while True:
        choice=raw_input("Enter n to play a new hand or r to replay the last hand or e to end the game:")
        if choice=='e':
            print("Game over!")
            break

        if choice not in 'nre':
            print("Enter  a valid option")
            continue
        turn=raw_input("Enter u to play the hand or enter c to let the computer play the hand:")
        if turn not in 'uc':
            print("Enter a valid option")
            continue
        if choice=='n':
            hand = dealHand(HAND_SIZE)
            if turn=='u':
                playHand(hand,wordList,HAND_SIZE)
            else:
                compPlayHand(hand,wordList,HAND_SIZE)
        elif choice=='r':
            if hand=={}:
                print("You have not played a hand yet. Please play a hand first")
            else:
                if turn=='u':
                    playHand(hand,wordList,HAND_SIZE)
                else:
                    compPlayHand(hand,wordList,HAND_SIZE)
        else:
            print("Game Over!")
            break



        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


