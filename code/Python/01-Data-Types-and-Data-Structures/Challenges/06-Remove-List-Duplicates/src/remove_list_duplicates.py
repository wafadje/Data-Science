"""
Remove duplicates from a list.
"""

def main():
    # TODO: create a list `source` with duplicates and print it.
    source = ['hello', 'world', 'hello']


    # TODO: remove the duplicates from `source` and store the result in a list `no_duplicates`. Print your result.
    no_duplicates = list(set(source))
    print(no_duplicates)



if __name__ == "__main__":
    main()
