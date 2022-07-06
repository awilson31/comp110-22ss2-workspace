"""EX03 - Wordle - A cute step toward Wordle."""

__author__ = "730440563"
def contains_char(word: str, chara: str) -> bool:

    assert len(chara) == 1
    INDEX = 0
    a = False
    while INDEX < len(word):
        if word[INDEX] == chara:
            a = True
        INDEX += 1
    return a        

def emojified(w: str, guess: str) -> str: 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(w) == len(guess)
    word: str = w
    gues: str = guess    
    INDEX = 0 
    str2 = ""
    while INDEX < 5:
        if gues[INDEX] == word[INDEX]:
            str2 += GREEN_BOX 
        else:
            gt = 0
            a = False
            while gt < 5:
                if gues[INDEX] == word[gt]:
                    a = True
                    gt += 1
                else: 
                    gt += 1
            if a == True:
                str2 += YELLOW_BOX
            else:
                str2 += WHITE_BOX
          
        INDEX += 1
    return str2

def input_guess(explen: int) -> str:
    gues: str = input("Enter a 5 character word: ")
    while len(gues) != explen:
        gues: str = input("That wasn't 5 characters! Try again: ")
    return gues

def main() -> None:
    secwor: str = "codes"
    turn = 1
    b = False
    while turn < 7:
        print(" === Turn " + str(turn) + "/6 ===")
        guess: str = input_guess(5)  
        emoji: str = emojified(secwor, guess)
        print(emoji)
        if guess == secwor:
            print("You won in " + str(turn) + "/6 turns!")
            exit()
        else: 
            turn += 1
    print(" X/6 - Sorry, try again tomorrow!")
main()
if __name__ == "__main__":
    main()