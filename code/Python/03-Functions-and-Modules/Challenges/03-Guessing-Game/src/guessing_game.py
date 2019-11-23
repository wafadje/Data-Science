import random

"""
A very simple guessing game
"""

def main():
	count = 0
	while True:
		 
		number_to_guess = int(input("What's your guess between 1 and 99? "))
		random.seed(3)
		result = random.randint(1, 99)
		print(result)
	
		if result < number_to_guess :
			print("Too high!")
		elif result > number_to_guess :
			print("Too low!")
		elif result == number_to_guess :
			print("Congratulations, you've got it!")
			break
		else : 
			print("Please enter a valid number !")
		count += 1

	print("And it only took you only {} trials!".format(count))


if __name__ == '__main__':
    main()
