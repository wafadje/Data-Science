from datetime import datetime as dt
import time

# TODO: Display the various DateTime formats
current_date_and_time = dt.now()
#current_date_and_time = dt.now().strftime("%Y-%m-%d %H:%M"))

current_year= current_date_and_time.year

month_of_year = current_date_and_time.month

week_number_of_the_year = current_date_and_time.strftime("%W")
#print(week_number_of_the_year)

weekday_of_the_week = current_date_and_time.strftime("%W")

day_of_year = dt.date(2012, 12, 1) - dt.date(2012, 1, 1)
print(day_of_year)

day_of_the_month = dt.date.month

day_of_week = dt.date.weekday

# TODO: Convert a string to datetime

datetime_obj = dt.strptime("2018-02-02", "%Y-%m-%d")
#print(datetime_obj)

# TODO: Display the date of the first Monday of a given week



# TODO: Get the number of days between two dates

delta = dt.date(2008, 8, 18) - dt.date(2008, 9, 26)
print(delta)


# TODO: Get the last day of a specified year and month


# TODO: Convert a date to the timestamp


# TODO: Print a string five times, delay three seconds


# TODO: Get last modified information of a file `text.txt`(to create)
