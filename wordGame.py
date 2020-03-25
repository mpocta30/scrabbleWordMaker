import sys
import json
import enchant
import itertools

from pandas.io.json import json_normalize

# Constants
jsonFile = open("wordGame.json")
checkDictionary = enchant.Dict("en_US")
pointDirectory = json.load(jsonFile)

# Final message variables
highScore = 0
finalWord = ''
highWordFound = False


# Description: Filter words based on score and if valid
# Param: {Tuple} word Collection of letters making the word
def wordFilter(word):
    global highScore, finalWord, highWordFound

    # Get the current word score
    curScore = 0
    word = ''.join(word)
    for letter in word:
        curScore += pointDirectory[letter]

    if(checkDictionary.check(word)):
        highScore = curScore
        finalWord = word
        highWordFound = True
        return True
    else:
        return False


# Description: Sort the list of letters by point value
# Param: {Character} x Current list value to sort
def sortLetters(x):
    pointTotal = 0
    for letter in x:
        pointTotal += pointDirectory[letter]
    return pointTotal


# The alphabet to loop through
alphabet = list(pointDirectory.keys())

highScore = 0
curScore  = 0
finalWord = ''

for i in range(2, 10):
    # Reset values
    highScore = 0
    finalWord = ''
    highWordFound = False

    # Duplicated alphabet
    dupAlphabet = alphabet*i

    # Create a list of possible word combinations
    dupList = sorted(itertools.combinations(dupAlphabet, i), key=sortLetters, reverse=True)

    j = 0
    curDupList = iter(dict.fromkeys(itertools.islice(dupList, 50000)))
    while curDupList and not highWordFound:
        for word in curDupList:
            if wordFilter(word):
                break
        curDupList = iter(dict.fromkeys(itertools.islice(dupList, 50000)))



    # j = 0
    # curDupList = list(itertools.islice(dupList, 100))
    # while highWordFound == False and curDupList:
    #     # Remove duplicates from list
    #     for curWord in list(dict.fromkeys(curDupList)):
    #         if(wordFilter(curWord)):
    #             break

    #     curDupList = list(itertools.islice(dupList, 100))
    #     j+=1
        

    # for comb in curList:
    #     # Get the current word score
    #     curScore = 0
    #     for letter in comb:
    #         curScore += pointDirectory[letter]

    #     # Check if the word is valid and if the score is higher than high score
    #     # update high score
    #     curWord = ''.join(comb)
    #     if(curScore > highScore):
    #         highScore = curScore
    #         finalWord = curWord

    print('\n\tResults for ' + str(i))
    print('\t-------------')       
    print('\tWord: ' + finalWord)
    print('\tScore: ' + str(highScore) + '\n')