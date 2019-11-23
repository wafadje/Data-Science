"""
A couple of exercises to become fluent with list comprehensions
"""

def main():
    # TODO: Find all of the numbers from 1-1000 that are divisible by 7
    number_divisible_7 = [i for i in range(1, 1001) if i % 7 == 0]
    #print(number_divisible_7)


    # TODO: Find all of the numbers from 1-1000 that have a 3 in them
    number_with_3 = [ i for i in range(1, 1001) if str(i).find('3') != -1]
    #print(number_with_3)

    # TODO: Count the number of spaces in a string
    words = "jfdi nifzleniz enfpoze, fpoze, po ,kh qa"
    count_space = len([element for element in words if element == " " ])
    #print(count_space)

    # TODO: Remove all of the vowels in a string [make a list of the non-vowels]
    vowel = ['a', 'e', 'u', 'i', 'y', 'o']
    word = "jfdinifzlenizenfpoze,fpoze,po,khqa"
    non_vowels = [i for i in word if i not in vowel]
    #print(non_vowels)


    # TODO: Find all of the words in a string that are less than 4 letters
    words = "jfdi nifzleniz enfpoze, fpoze, po ,kh qa"
    
    result = [word for word in words.split(" ") if len(word) < 4]
    #print(result)

    # TODO: Use a dictionary comprehension to count the length of each word in a sentence.
    sentence = "jfdi nifzleniz enfpoze, fpoze, po ,kh qa"

    count_word =  {key:len(key) for key in sentence.split(" ")}
    #print(count_word)

    # TODO: Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
    nested_list = [i for i in range(1,1001) if i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 ]
    #print(nested_list)

    # TODO: For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by.
    highest_digit = [ for i in range(1,10) for k in range(1, 10) if k % i == 0 ]
    print(highest_digit)

if __name__ == '__main__':
    main()
