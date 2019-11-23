"""
Counts the number of odd and even numbers in a sequence
"""

def main():
    numbers = [21, 82, 12, 69, 1, 91, 89, 6, 31, 13, 85, 10,
    43, 89, 13, 50, 87, 14, 97, 52]

    # TODO: write a loop to classify numbers in even or odd lists and display your results.
    even_list = []
    odd_list = []

    for number in numbers :
    	if number % 2 == 0 :
    		even_list.append(number)
    	else :
    		odd_list.append(number)
    print(even_list)
    print(odd_list)


    # TODO: do the same with list comprehensions and display your results.
    even_list_comprehensions = [num for num in numbers if num % 2 == 0]
    print(even_list_comprehensions)
    odd_list_comprehensions = [num for num in numbers if num % 2 != 0]
    print(odd_list_comprehensions)


if __name__ == '__main__':
    main()

