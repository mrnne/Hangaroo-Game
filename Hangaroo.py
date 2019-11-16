def hangaroo(secretWord):
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 10
    wordGuessed = False
    
    print ('Welcome to Hangaroo!')
    print ('Guess a word that is ',intro,' letters long.')
    print ('_______________________________________________________________')

    while mistakesMade > 0 and mistakesMade <= 10 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ', str(mistakesMade), ' guesses left.')
        print ('Available letters: ', getAvailableLetters(lettersGuessed))
        guess= input('Please guess a letter: ')
        guesslower= guess.lower()
        if guesslower in secretWord:
            if guesslower in lettersGuessed:
                print ("Sorry :-( You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
                print ('_______________________________________________________________')
            else:
                lettersGuessed.append(guesslower)
                print ('Good guess :-) : ', getGuessedWord(secretWord, lettersGuessed))
                print ('_______________________________________________________________')
        else: 
            if guesslower in lettersGuessed:
                print ("Sorry :-( You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
                print ('_______________________________________________________________')
            else:
                lettersGuessed.append(guesslower)
                mistakesMade -= 1
                print ('Hmp :-\ That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
                print ('_______________________________________________________________')
       
        
    if wordGuessed == True:
        print ('Congratulations, you guessed it! The word was', secretWord)
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was', secretWord,'.', 'Try again next time')
    return


hangaroo("basketball")