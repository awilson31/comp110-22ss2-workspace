"""EX01 - Chardle - A cute step toward Wordle."""

__author__ ="730440563"


word: str = input("Enter a five letter word ")
chara: str = input("Enter a single character ")
print("Searching for " + chara + " in " + word)

if chara == word[0]:
    print(chara + " found at index 0") 
if chara == word[1]:
    print(chara + " found at index 1")
if chara == word[2]:
    print(chara + " found at index 2")
if chara == word[3]:
    print(chara + " found at index 3")
if chara == word[4]:
    print(chara + " found at index 4")






    
