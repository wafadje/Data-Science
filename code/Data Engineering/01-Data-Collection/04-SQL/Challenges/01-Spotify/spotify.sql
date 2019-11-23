"""
. Selection
    In your terminal, open SQlite console and run the SQL script to create the database. Which tables does it contain?
    Activate headers in SQLite
    Select all rows and all columns from the table Album
    Select all rows and only the column Title from the table Album
    Select the 10 first rows and only the columns Title and ArtistId from the table Album
    Select all the unique ArtistId from the table Album
    Select all the unique Country from the table Customer
II. Filter
    Select all the customers with field State is null.
    Select all the customers FirstName, LastName, City, Country, State, and replace all empty values in State by "N/A".
    Select all the customers who have a Yahoo email address (ending by @yahoo.com, @yahoo.fr, @yahoo.be, etc.).
    Select all the Customers who have a Gmail or an Apple email address
    Select all the Customers who live in Bordeaux, Rome, or Rio de Janeiro
III. Count
    Count the number of Albums (= number of rows in Album table)
    Count the number of Customers with non missing field State
    Count the number of unique artists that released an album. Is it the same number of artists contained in Artist table?
    >select DISTINCT ArtistId, count() from Album;
    ArtistId|count()
    275|347
    >select DISTINCT ArtistId, count() from Artist;
    ArtistId|count()
    275|275
  
    No, it's not the same
IV. Order
    List all employees alphabetically (LastName, then FirstName in alphabetical order)
    > select LastName, FirstName from Employee order by LastName, FirstName;
    List FirstName of employees with their associated HireDate and sort it by decreasing HireDate.
    > select FirstName, HireDate from Employee order by HireDate DESC;
    List all employees FirstName, Title and BirthDate that are not General Manager and sort them by ascending Title and descending BirthDate
    > select FirstName, Title, BirthDate from Employee where Title != 'General Manager' order by Title, BirthDate DESC;
V. Aggregate
    Retrieve the number of albums released by ArtistId
    > select ArtistId, count() from Album group by ArtistId;
    Retrieve the possible different UnitPrice of a Track and the associated number of tracks at this price. Give this last column a correct name.
    >  select UnitPrice,
   ...> count() as number_track
   ...> from Track
   ...> group by UnitPrice;
    UnitPrice|number_track
    0.99|3290
    1.99|213
    Retrieve the list of Composer (non-missing) that wrote more than 20 songs and the number of songs they created (call the column nb_songs). Order the results by descending number of songs.
     select count(Name) as c, Composer
   ...> from Track
   ...> group by Composer
   ...> Having c > 20 and Composer != "";
   c|Composer
    25|Bill Berry-Peter Buck-Mike Mills-Michael Stipe
    31|Billy Corgan
    23|Chico Science
    23|Chris Cornell
    23|Gilberto Gil
    35|Jagger/Richards
    26|Kurt Cobain
    23|Miles Davis
    80|Steve Harris
    24|The Tea Party
    22|Titãs
    44|U2
"""
