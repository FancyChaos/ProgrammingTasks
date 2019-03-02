#!/usr/bin/env python
# The Dice rolling sim solution
import random
import sys

# python2 / python3 compatibility
if sys.version_info[0] == 2:
    input = raw_input

prologue = '''
Welcome to DiceRollingSim!

               (( _______
     _______     /\O    O\\
    /O     /\   /  \      \\
   /   O  /O \ / O  \O____O\ ))
((/_____O/    \\\\    /O     /
  \O    O\    / \  /   O  /
   \O    O\ O/   \/_____O/
    \O____O\/ )) mrf      ))
  ((

Create your own unique custom dice having N sides...

(lots of natural numbers are supported!)

...and throw it virtually like a boss!
'''


def input_dice_sides():
    '''ask user how many sides our dice shall have'''
    while True:
        print('Abort using CTRL-C')
        try:
            sides = int(input("How many sides shall your dice have?: "))
            break
        except ValueError:
            print('Please enter a valid number. Like 6')
        except Exception:
            raise

    return sides


def main():

    print(prologue)

    sides = input_dice_sides()

    # main loop: thow dice and ask user if he/she wants to throw another time
    while True:
        random_number = random.randint(1, sides)
        print("You rolled a: {}".format(random_number))
        roll_again = input("Do you want to roll again? */n : ")
        if roll_again == "n":
            break

    print('Dice rolling sim quit.')


# Because of good practise
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Dice rolling sim aborted.')
