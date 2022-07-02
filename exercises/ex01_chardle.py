"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730440563"


word: str = input("Enter a five letter word ")
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

chara: str = input("Enter a single character ")
if len(chara) < 1 or len(chara) > 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + chara + " in " + word)
int = 0 
if chara == word[0]:
    print(chara + " found at index 0") 
    int += 1
if chara == word[1]:
    print(chara + " found at index 1")
    int += 1
if chara == word[2]:
    print(chara + " found at index 2")
    int += 1
if chara == word[3]:
    print(chara + " found at index 3")
    int += 1
if chara == word[4]:
    print(chara + " found at index 4")
    int += 1

if chara in word:
    print(str(int) + " instance of " + chara + " found in " + word) 
else:
    print("No instances of " + chara + " found in " + word)
    