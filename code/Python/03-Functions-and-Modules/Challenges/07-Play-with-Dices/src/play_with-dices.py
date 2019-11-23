"""
 Prompt the user for a number between 2 and 12, and return the number of possibilities to achieve this score 
 while simultaneously throwing 2 dices.
Same question with a number n between 3 and 18 and 3 dices.
Generalize the question : ask the user for a number of dices nbd (between 1 and 10) and the score s he wants 
to achive (s is between nbd and 6 * nbd), and return the number of possibilities to achieve the score s with nbd dices.
Try to solve the same question recursively.
"""

# TODO: import random module
import random

# TODO: `score_2_dices()`
def score_2_dices():
	number = int(input("Please enter a number between 2 and 12"))


# TODO: `score_3_dices()`


# TODO: `score_n_dices()`


# TODO: `score_n_dices_recursively()`


def main():
	score_2_dices()

if __name__ == '__main__':
    main()

