"""
Count word occurences.
"""

def main():
    """
    A function that asks for some text and displays the word occurences by descending order.
    """
    # TODO: ask the user to input some `text`
    texts = input("Enter your text without forgetten the space between words ").split(" ")


    # TODO: count the number of occurences of each word in the text
    dict_word_count = {}

    for text in texts :
    	dict_word_count[text] = texts.count(text)

    liste_word_key = list(dict_word_count.keys())
    liste_word_value = list(dict_word_count.values())
    #liste_word = zip(liste_word_value, liste_word_key)
    # TODO: sort by descending order of occurences and display the result
    
    for occurance, word in sorted(zip(liste_word_value, liste_word_key), reverse = True) : 
    	print(occurance, word)


if __name__ == '__main__':
    main()
