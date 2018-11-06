word = input("Enter english word: ")

word = word.lower()

VOWELS = "aeiou"

while word != "quit":
    if word[0] in VOWELS:
        word += "way"
        print (word)
    
    else:    
        vowels_in_word = ""
        for i,ch in enumerate(word):
            if ch in VOWELS:
                print(word[i:]+word[:i]+"ay")
                break
            
    word = input("Enter english word: ")

    word = word.lower()