"""
Ask for a number and return only the elements in the list below that number.
"""

def main():
    full_list = [1, 2, 3, 5, 8, 10, 11, 11, 13, 21, 22, 29, 29, 30, 34, 55, 59, 64, 67, 72, 89, 93, 99]

    # TODO: ask for the user to enter a number below 100 as `filter`
    input_filter = int(input("Please enter a number below 100"))


    # TODO: create the `list_filtered` and populate it. Print out your result.
    list_filtered = []
    for element in full_list:
    	if element < input_filter :
    		list_filtered.append(element)
    print(list_filtered)


if __name__ == '__main__':
    main()

