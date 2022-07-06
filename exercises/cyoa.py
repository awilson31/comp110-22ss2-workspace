__author__ = "730440563"

import random
player = ""
points = 0
frown: str = "\U0001F61F"
congrats: str = "\U0001F973"
smile:str = "\U0001F642"
def main() -> None:
    #print(random.choice(randnum))
    greet()
    answ: str = input(" Would you like to play? Yes or No ")
    if answ == "No":
        print("Come back when you're ready to play.")
        print("Points earned 0" + frown)
        exit()
    else:
        print("Thank you for continuing to play!" + smile)
    he: str = input("How would you like to play the game? Easy or Hard ")
    if he == "Easy":
        guesseasy()
    else:
        guesshard()
    game_loop: str = input("Would you like to continue playing? Yes or No ")
    if game_loop == "Yes":
        print("Youve earned " + points + " points")
        he: str = input("How would you like to play the game? Easy or Hard ")
    if he == "Easy":
        guesseasy()
    elif he == "Hard":
        guesshard()
    else:
        print("Thank you for playing, " + player)
        print("Youve earned " + points + " points")
        
        

def greet() -> None:
    print("Welcome to the number guessing game!")
    player2: str = input("What is your name? ")
    player = player2


def guesseasy() -> int:
    points = 0
    randnum = random.randint(1, 5)
    ai: str = input(player + ",guess a number between 1-5: ")
    if int(ai) > randnum:
        points += 1
        print("too high!")
    if int(ai) < randnum:
        points += 2
        print("too low")
    if int(ai) == randnum:
        points += 3
        print("You got the secret number" + congrats)

def guesshard() -> int:
    points = 0
    randnum = random.randint(1, 10)
    ai: str = input(player + ", guess a number between 1-10: ")
    if int(ai) > randnum:
        points += 1
        print("too high!")
    if int(ai) < randnum:
        points += 2
        print("too low")
    if int(ai) == randnum:
        points += 3
        print("You got the secret number" + congrats)
main()
if __name__ == "__main__":
    main()
