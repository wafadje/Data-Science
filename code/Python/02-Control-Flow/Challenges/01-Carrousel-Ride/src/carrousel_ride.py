"""
Height requirements ckecking in a theme park.
"""

def main():
    # TODO: ask for user's size in centimeters and store the result in a variable : height
    height = int(input("Would you please enter your height in cm "))


    # TODO: print "Sorry, you're too small for this ride. Try another carrousel."
    # if height inferior to 100 (excluded)
    if height < 100 :
    	print("Sorry, you're too small for this ride. Try another carrousel.")


    # TODO: print "Enjoy your ride!" if height is superior to 100 (included) and 150 (included)
    if 100 <= height < 150 :
    	print("Enjoy your ride!")


    # TODO: print "Sorry, you're too tall for this one!" if you height is over 150 (excluded)
    if 150 < height :
    	print("Sorry, you're too tall for this one!")

if __name__ == '__main__':
    main()
