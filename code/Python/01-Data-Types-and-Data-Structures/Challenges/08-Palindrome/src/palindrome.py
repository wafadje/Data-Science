"""
Determine if a word is a palindrome.
"""

def main():

	chaine = "kayak"

	if chaine[:] == chaine[::-1] : 
		print("chaine is a palindrome")
	else : 
		print("word is not a palindrome")

if __name__ == "__main__":
    main()
