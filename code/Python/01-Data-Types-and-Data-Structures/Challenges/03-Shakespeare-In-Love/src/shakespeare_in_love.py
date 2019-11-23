"""
String manipulations with Shakespeare
"""

def main():
    # TODO: print the correct version of this string: capitale for the first letter and then lowercase characters.
    sentence = "a fOol thiNks hImseLf to bE wiSe, buT a wise mAn knoWs himself to BE a fool."
    # Bonus point if you find the author :-)
    print(sentence.capitalize())


    # TODO: print the number of "fool" occurancies in the previous sentence
    counts = sentence.count("fool")
    print(counts)


    # TODO: print the total length of this shakesperean play (use a variable `title_length` to calculate it)
    first_word = "As"
    second_word = "You"
    third_word = "Like"
    fourth_word = "It"
    
    title = first_word + second_word + third_word + fourth_word
    title_length = len(title) + 3

    # TODO: print a log message with the variables above. It should have the format:
    # Ophelia checked the page http://shakespeare.com/play/Hamlet/casting at 18:45.
    username = "Rosalinde"
    time = "09:23"
    url = "http://shakespeare.com/play/asyoulikeit/casting"
    access = "checked the page"

    log_message = username + " " + access + " " + url + " " + "at " + time +"."
    print(log_message)

    # TODO: print "According to the rumor, Queen Elizabeth liked Shakespeare plays, especially 'Much Ado About Nothing'."
    # using the following variable and .format
    sent = "According to the rumor, Queen Elizabeth liked {} plays, especially {}."
    print(sent.format("Shakespeare", "'Much Ado About Nothing'"))


if __name__ == "__main__":
    main()
