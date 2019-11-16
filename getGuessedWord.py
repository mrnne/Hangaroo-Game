def getGuessedWord(secretWord, lettersGuessed):
    number = 0
    blank = ['_ '] * len(secretWord)

    for a, b in enumerate(secretWord):
        if b in lettersGuessed:
            number += 1
            blank.insert(number-1,b)
            blank.pop(number)
            if number == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            number += 1
            blank.insert(number-1,'_')
            blank.pop(number)
            if number == len(secretWord):
                return ''.join(str(e) for e in blank)
        