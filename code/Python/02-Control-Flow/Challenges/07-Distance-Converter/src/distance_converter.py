"""
A programm to convert distances between meters and miles
"""

def main():

	distance = int(input("Please enter a distance to convert"))
	unit = input("What is the unit")

	km = ['KM', 'Km', 'km']
	miles = ['miles', 'Miles', 'MILES']

	if unit in km :
		print("the distance in miles is {} ".format(distance * 0.621371192 ))
	elif unit in miles :
		print("the distance in km is {} ".format(distance * 1.609344))
	else :
		print("PLease enter a valid unit")



if __name__ == '__main__':
    main()
