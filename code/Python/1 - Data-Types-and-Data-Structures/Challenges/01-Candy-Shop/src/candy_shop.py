"""
Manage a candy shop's stock
"""

def main():
    # The initial stock of the candy shop
    candy_stock = 45000

    # The Monday delivery amount
    monday_delivery = 3000

    # TODO: add the Monday delivery to the stock
    candy_stock += monday_delivery


    # TODO: decrease the stock of 25% after the Christmas purchase
    candy_stock *= 0.75 

    # TODO: substact 1500 candies bought for the school celebrations
    candy_stock -= 1500

    # TODO: increase the stock of 7% after a special delivery of Christmas cracker
    candy_stock *= 1.07 

    # TODO: print the final amount of the stock
    print(candy_stock)

if __name__ == '__main__':
    main()
