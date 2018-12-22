# Problem Set 2, hangman.py


# Hangman Game
# -----------------------------------

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
    guessed =   True
    for i in secret_word:
       if i not in letters_guessed:
           guessed = False
           break
    return guessed
      
#print(is_word_guessed("apple",["a","p","e"]))
            



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    temp_secret = secret_word
    for i in temp_secret:
        if i not in letters_guessed:
            temp_secret = temp_secret.replace(i," _")
        else:
            temp_secret = temp_secret.replace(i, " "+i)

    return temp_secret

#print (get_guessed_word("apple",["a","l","x"]))




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters_remaining = alphabet
    for i in letters_guessed:
        if i in alphabet: 
            letters_remaining = letters_remaining.replace(i,"")
    return letters_remaining

#print (get_available_letters(["a","b"]))


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

    unique = len(set(secret_word))
    guess = 6
    warnings = 3
    
    print ("--------------------")
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(secret_word) , " letters long.")
    
    
    letters_guessed=[]
    
    
    while guess>0: 
        print ("--------------------")
        print ("You have " , guess , " guesses left.")
        print ("Available letters: ", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ").lower()
        
        #check if it's a valid entry
        if letter in letters_guessed:
            print("Oops! You already guessed that.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break
        elif len(letter)>1:
            print("Oops! That's more than one letter.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break
            
        # give a warning if it is not a letter
        elif not letter.isalpha():
            print("Oops! That is not a letter.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break

        else:
            
            letters_guessed.append(letter)
            
            if letter in secret_word:
                print("Good guess:", get_guessed_word(secret_word,letters_guessed))
                if (is_word_guessed(secret_word,letters_guessed)):
                    print("Congratulations, you won! Your total score for this game is:", guess*unique)
                    break
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
                if letter in "aioue":
                    guess-=2
                else:
                    guess-=1
                if guess<1:
                    print("Sorry, you ran out of guesses. The word was" , secret_word,".")
                    break

        
   
        
        
        
        
        
    





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
    word = my_word.replace(" ","")
    if len(word) != len(other_word):
        return False
    for i in range (len(other_word)):
        if other_word[i] in word:
            if other_word[i] != word[i]:
                return False
        else:
            if other_word[i] != word[i] and word[i] !="_":
                return False
    return True

#print(match_with_gaps("t__t", "tart"))
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = []
    for i in wordlist:
        if match_with_gaps(my_word,i):
            possible_words.append(i)
    return possible_words


#print(show_possible_matches("t__t"))
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
    secret_word = "tact"
    unique = len(set(secret_word))
    guess = 6
    warnings = 3
    
    print ("--------------------")
    print ("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(secret_word) , " letters long.")
    
    
    letters_guessed=[]
    
    
    while guess>0: 
        print ("--------------------")
        print ("You have " , guess , " guesses left.")
        print ("Available letters: ", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ").lower()
        
        #check if it's a valid entry
        if letter in letters_guessed:
            print("Oops! You already guessed that.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break
        elif len(letter)>1:
            print("Oops! That's more than one letter.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break
            
        # give a warning if it is not a letter
        
        elif letter=="*":
            print("Possible matches= ", show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
        elif not letter.isalpha():
            print("Oops! That is not a letter.")
            if warnings > 0:
                warnings -= 1
                print("You now have", warnings, "warnings left! :", get_guessed_word(secret_word,letters_guessed))
            elif warnings==0 and guess>1:
                guess -= 1
                print("You have no warnings left, so you lose one guess:", get_guessed_word(secret_word,letters_guessed))
            else:   
                print ("Sorry, you ran out of guesses. The word was", secret_word,".")
                break

        else:
            
            letters_guessed.append(letter)
            
            if letter in secret_word:
                print("Good guess:", get_guessed_word(secret_word,letters_guessed))
                if (is_word_guessed(secret_word,letters_guessed)):
                    print("Congratulations, you won! Your total score for this game is:", guess*unique)
                    break
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word,letters_guessed))
                if letter in "aioue":
                    guess-=2
                else:
                    guess-=1
                if guess<1:
                    print("Sorry, you ran out of guesses. The word was" , secret_word,".")
                    break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
