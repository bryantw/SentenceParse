# In the programming language of your choice, write a program that parses a sentence and replaces each word with the following: first letter, number of distinct characters between first and last character, and last letter. Words are separated by spaces or non-alphabetic characters and these separators should be maintained in their original form and location in the answer.

# Examples:

# 1 “Smooth” becomes “S3h”
# 2 “Space separated” becomes “S3e s5d”
# 3 “Dash-separated” becomes “D2h-s5d”
# 4 “Number2separated” becomes “N4r2s5d”
# We will be looking for accuracy, efficiency, and solution completeness. Please include this problem description in a comment at the top of your solution. The problem is designed to take about 1-2 hours and will be used as a conversation point in the verbal assessment part of your interview.

def ParseSentence(sentence):
    length = len(sentence)
    # Sentences with only two characters will be edited
    if length <= 2:
        return sentence

    parsedSentence = ''
    findUniqueCharacters = False
    # Sets do not allow duplicate values
    uniqueCharacterSet = set()

    for x in range(length):
        if sentence[x].isalpha():
            if findUniqueCharacters:
                # Add current character to set
                uniqueCharacterSet.add(sentence[x])

                # Check if the end is next or a not alphabetic
                if (x + 2 >= length or not sentence[x+2].isalpha()):
                    findUniqueCharacters = False
                    parsedSentence += str(len(uniqueCharacterSet))

                    # Clean set
                    uniqueCharacterSet = set()
            else: # Parsing in an alphabetic
                parsedSentence += sentence[x]

                # Collect unique character count IFF there more alphabetics
                if x+2 < length and sentence[x+1].isalpha() and sentence[x+2].isalpha():
                    findUniqueCharacters = True    
        else: # Parsing the non-alphabetic
            parsedSentence += sentence[x]
            findUniqueCharacters = False

    return parsedSentence

print(ParseSentence('')) # ''
print(ParseSentence('a')) # 'a'
print(ParseSentence('5')) # '5'
print(ParseSentence('bc')) # 'bc'
print(ParseSentence('Smooth')) # 'S3h'
print(ParseSentence('Space separated')) # 'S3e s5d'
print(ParseSentence('Dash-separated')) # 'D2h-s5d'
print(ParseSentence('Number2separated')) # 'N4r2s5d'
print(ParseSentence('5a-bc def-')) # '5a-bc d1f-'
print(ParseSentence('5a-bc def-lh')) # '5a-bc d1f-lh'