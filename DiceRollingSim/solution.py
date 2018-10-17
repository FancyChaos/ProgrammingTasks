## The Dice rolling sim solution ##
import random


def main():
    sides = int(input("How many sided should the dice have?: "))
    while True:
        random_number = random.randint(1, sides)
        print("You rolled a: {}".format(random_number))
        roll_again = input("Do you want to roll again?: ")
        if roll_again == "n":
            break


# Because of good practise
if __name__ == "__main__":
    main()
