"""
Count the number of upper and lower characters in a given text.
"""
def count_char(text):
	'''
	Count the number of upper and lower characters in a given text
	Parameters:
	-----------
	a text : String
	
	Return:
	------
	number of upper characters : int
	number of lower characters : int
	'''
	upper = 0
	lower = 0

	for txt in text.split(" "):
		if txt.isupper():
			upper += 1
		elif txt.islower():
			lower += 1
	return upper, lower
