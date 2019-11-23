
'''
 Write a Python program using lambda and map(), 
 which returns a list with 2-tuples. 
 Each tuple consists of the order number and the total price (quantity * price per item).
The total price of a given order should be increased by 10 euros if the value of the order is less than 100 euros.
 '''


orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]


order = 100


results =  map(lambda x : (x[0], x[2] * x[3]), orders)


for result in results:
	if result[1] < 100 :
		result[1] +10
	else :
		result[1]
