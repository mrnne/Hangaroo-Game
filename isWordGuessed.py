def isWordGuessed(secretWord, lettersGuessed):

    number = 0
    for a, b in enumerate(secretWord):
    	if b in lettersGuessed:
    		number += 1
    if number == len(secretWord):
    	return True
    else:
    	return False
