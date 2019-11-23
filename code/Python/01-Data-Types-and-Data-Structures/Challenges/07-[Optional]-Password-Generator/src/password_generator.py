"""
Generate a password of the size given by a user.
"""
import random
import string

def main():
	valeur = int(input("enter a value"))
	char = string.digits + string.ascii_letters + string.punctuation

	word = ''.join(random.sample(char, valeur))
	print(word)

if __name__ == "__main__":
    main()
