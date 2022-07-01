"""EX02 - One-Shot wordle - A cute step toward Wordle."""

__author__ ="730440563"

w: str = "python"
gues: str = input("What is your 6-letter word guess? ")
g = 0
while g != 6: 
    if len(gues) == 6:
        g = 6 
        break
    gues: str = input("That was not 6 letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
INDEX = 0 
str2 = ""
while INDEX < 6:
    if gues[INDEX] == w[INDEX]:
        str2 += GREEN_BOX 
    else:
        gt = 0
        a = False
        while gt < 6:
            if gues[INDEX] == w[gt]:
                a = True
                gt += 1
            else: 
                gt += 1
        if a == True:
            str2 += YELLOW_BOX
        else:
            str2 += WHITE_BOX
          
    INDEX += 1
print(str2) 
             
if gues == w:
    print("Woo! You got it!")
else:
    if gues != w:
        print("Not quite. Play again soon!")  
