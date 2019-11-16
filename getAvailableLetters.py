def getAvailableLetters(lettersGuessed):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def availableLetters(L1, L2):
        L1Start = L1[:]
        for e in L1:
            if e in L1Start:
                L2.remove(e)
        return ''.join(str(e) for e in L2)

    return availableLetters(lettersGuessed, alphabet2)

