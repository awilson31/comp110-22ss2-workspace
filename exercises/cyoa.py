__author__ = "730440563"

def main() -> None:
    randnum = [1, 2, 3, 4, 5]
    print(random.choice(randnum))
    points = 0
#if __name__ == "__main__":
    main()
def greet() -> None:
    greet: str = "Welcome to the number guessing game! Your job is to guess a number from 1-5."
    print greet 
    player: str = input("What is your name? ")
    return player

guess: str = input(player + ", guess a number between 1-5: ")
    if guess > randnum:
        points += 1
        print("too high!")
    if guess < randnum:
        points += 2
        print("too low")
    if guess == randnum:
        points += 3
        print("You got the secret number")
