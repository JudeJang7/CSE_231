###########################################################
# Programming Project #3
#
#
#
# Prompt user for string
#
# Search for unique vowels in string
#
# Concatenates vowel into an empty string
#
# Search for consonants after the last vowel
#
# Concatenates unique consonants into an empty string
# 
# Print concatenated vowels and consonants as well as length
# 
###########################################################

VOWELS = "aeiou" 
# Characters that are being searched for in string
vowels = ""
# Holds unique vowels
consonants = "" 
# Holds unique consonants

while len(vowels) < 5 and len(consonants) < 5: 
# Iterates through all the characters in the inputted word    

    word_input = input("Input a word: ")
    # Prompt user to input a string

    for index, character in enumerate(word_input):
    # Iterates through string
        if character in VOWELS:
        # If character is a vowel, proceed    
            last_vowel = index
            # Holds index for last vowel
            if character not in vowels:
            # Checks to see if vowel is unique   
                vowels += character
                # Concatenates vowel into an empty string
                   
    for character in word_input[last_vowel:]:
    # Iterates through rest of string after the last vowel    
        if character not in vowels:
        # Checks to see character is not a vowel    
            if character not in consonants:
            # Checks to see consonant is unique    
                consonants += character
                # Concatenates consonant into an empty string
                         
            
                       
print("\n"+"="*12)   
# Formats =        
print("{:8s}{:7s} | {:12s}{:7s}".format\
      ("vowels","length","consonants","length"))
# Formats \
print("{:8s}{:<7d} | {:12s}{:<7d}".format\
      (vowels,len(vowels), consonants, len(consonants)))
# Prints concatenated vowels and consonants as well as their lengths