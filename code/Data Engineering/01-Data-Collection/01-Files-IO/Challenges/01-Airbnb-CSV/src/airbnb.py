import os, csv

"""
The input/airbnb.csv file contains an extract of 100 vacation rentals.
1. Import the data in a list and play with it :
    write your name as the Host Name of the ad "3-pièces proche Montorgueil Paris"
    change the Last Review date of the ad n°3305756 to 2019-01-07
    increase the price of all Philippe's ad to 250
    retrieve all the ads around Ménilmontant and store them in a file input/menilmontant.csv keeping only the Id,
     Name and Price info
    remove the two ads close to Notre-Dame from the list
2. Create a Rental class and instanciate all the ads in the input/airbnb.csv file.
    select only 10 ads near Panthéon with the highest numbers of reviews and store them in a input/pantheon.bin
     binary file
    open the file again and delete all the Private Rooms
    convert the remaining content of input/pantheon.bin into input/pantheon.csv file.
"""
#class Rental():

def main():

	filepath_down = os.path.join('..', 'input/airbnb.csv')
	filepath_down_2 = os.path.join('..', 'input/menilmontant.csv')

	with open(filepath_down, 'r') as f:
		reader = csv.reader(f,  delimiter=';')
		elements = [element for element in reader]
		#print(elements)

	with open(filepath_down, 'a') as f:
		writer = csv.writer(f)
		for element in elements:
			for e in element:
				print(e.split(","))


	'''with open(filepath_down, 'w') as f:
		writer = csv.writer(f)
		for element in elements:
			if element[1] != 'Chambre indépendante - Notre-Dame' and element[1] != 'Charming flat close to Notre-Dame':
				writer.writerow(element)'''

	'''with open(filepath_down_2, 'w') as f:
		writer = csv.writer(f)
		for element in elements:
			if "Ménilmontant" in element :
				element = [element[0], element[1], element[9]]
				writer.writerow(element)'''



	'''with open(filepath_down, 'a') as f:
		writer = csv.writer(f)
		for element in elements:
			if "Philippe" in element :
				price = element[9]
				#print(int(price))
				price = int(price) + 250
				element[9] = price
				print(element)'''


	'''with open(filepath_down, 'a') as f:
		writer = csv.writer(f)
		for element in elements:
			if "3305756" in element :
				element[12] = '2019-01-07'
				print(element)'''
	
	

	
	'''with open(filepath_down, 'a') as f:
		writer = csv.writer(f)
		for e in elements:
			if "3-pièces proche Montorgueil Paris" in e :
				e[3] = "Wafa"
				print(e)'''
	

    
if __name__ == "__main__":
    main()
