#!/usr/bin/env python
# Solution to the number guessing game
import random


def main():
    secret_number = random.randint(1, 10)
    while True:
        print("A secret number between 1 and 10 occured!")
        guess = int(input("What is your guess?: "))

        if guess == secret_number:
            print("You won!")
            play_again = input("Do you want to play again?: ")
            if play_again == "n":
                break
            secret_number = random.randint(1, 10)
        elif guess < secret_number:
            print("The secret number is bigger!")
        elif guess > secret_number:
            print("The secret number is smaller!")


# Good practice
if __name__ == "__main__":
    main()
