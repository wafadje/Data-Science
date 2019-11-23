"""
1. Back up your database

Copy sf_catalogue.csv into sf_catalogue.csv to create a backup, just in case you erase everything in the file :-)
2. Write functions to interact with the .csv database

    Write a function load_csv(filepath) to store the content of sf_catalogue.csv in a list data.

    Write a function log_csv(filepath) to add a Timestamp and a Username to sf_catalogue.csv. The Timestamp value shoud be the current time for each row. The Username value is admin_add for existing rows.

The content of sf_catalogue.csv should now look like this:

Timestamp,Username,Title,Publication_year,Author
2019-01-13 17:51:47,admin_add,Banquets of the Black Widowers ,1984,I. Asimov
2019-01-13 17:51:47,admin_add,Casebook of the Black Widowers,1980,I. Asimov
...
2019-01-13 17:51:47,admin_add,The Rules of Names,1964,U. K. Le Guin
2019-01-13 17:51:47,admin_add,The Tombs of Atuan ,1971,U. K. Le Guin

Hint: you may need to use datetime.strftime(). Check the documentation !

    Write a function add_book(username, title, date, author) to add a book to sf_catalogue.csv with the appropriate username and timestamp.

    Write a function get_book_info(title) returning the informations on a given book. Don't forget to manage the case of a wrong input!

    Write a function remove_book(title) that removes a given book in sf_catalogue.csv. Don't forget to manage the case of a wrong input!

3. Write an interactive program

Create a menu in the main() function. The program should work like this:

Hello, what's you name ?
>> vivadata
Thank you vivadata ! What do you want to do with you catalogue ?
1. Add a reference
2. Get information on a reference
3. Delete a reference
4. Exit the program
>> 1

Which reference do you want to add ?
>> Prince of Chaos
Who is the author ?
>> Roger Zelazny
When was it written ?
>> 1991
Thank you, the reference has been added to the database !

Do you want to do something else ?
1. Add a reference
2. Get information on a reference
3. Delete a reference
4. Exit the program
>> 2

Which reference are you interested in ?
>> The World of Nitrogen
Sorry, this reference is not in our database, try another one !
>> Tales of the Black Widowers
This book was written by I. Asimov in 1974
It has been added in the database by admin_add on Jan 13, 2018 at 17:51:47.

Do you want to do something else ?
1. Add a reference
2. Get information on a reference
3. Delete a reference
4. Exit the program
>> 3

Which reference do you want to delete ?
>> Project Pendulum
This reference has been removed from the database !

Do you want to do something else ?
1. Add a reference
2. Get information on a reference
3. Delete a reference
4. Exit the program
>> 4

Thank you vivadata, hope to see you soon !

Hint: do we really need to reload the data and write in the .csv file at each step?
Bonus: put everything together in a Book class

    Create the Book class in book.py. Add the __init__() method with the corresponding attributes.
    Use the previous functions to create useful instance methods to your class: add(), get_info() and remove().
    Use load_csv() to instanciate all the books in the main() function. Do not forget to import your Book class.
    Play with your books and save your results in sf_catalogue.csv before ending the program.
    Modify you program to work with a sf_catalogue.bin database, where your books are directly stored in a binary format
"""

def main():
    pass
    
if __name__ == "__main__":
    main()
