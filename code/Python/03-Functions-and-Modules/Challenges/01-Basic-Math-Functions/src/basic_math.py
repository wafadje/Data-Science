# TODO: a function `total()` that calculates the sum of a list of numbers.
def total(numbers):
	'''Calculates the sum of a list of numbers 
	Parameteres : 
	------------
	numbers = list of int
	Return:
	------
	the sum of the list number : int or float 
	'''
	list_sum = 0
	for number in numbers :
		list_sum += number
	return list_sum


# TODO: a function `mean()` that calculates the mean of a list of numbers.
def mean(numbers):
	'''Calculates the mean of a list of numbers 
	Parameteres : 
	------------
	num = list of int
	Return:
	------
	the mean of the list number : int or float 
	'''
	list_sum = 0
	for number in numbers :
		list_sum += number
	return list_sum / len(numbers)
