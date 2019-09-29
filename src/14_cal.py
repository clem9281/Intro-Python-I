"""
le allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

# I'm a little confused, is this meant to take in user imput or command line args? The way it is written seems like command line args but it also says user input? It's got sys imported for me so we're going to go with command line args

import sys
import calendar                      
from datetime import date, datetime 
today = date.today()
month=today.month
year = today.year
args = sys.argv 
length = len(args)

# since we set the month and year to today already I don't believe I need to actually need to check the len(args) == case
if (length == 2):
	# make a list out of calendar.month_name in order to use the index method to find the args string. make sure it's in the right format: first letter capitalized'
	month = list(calendar.month_name).index(args[1].capitalize())
elif(length == 3):
	month = list(calendar.month_name).index(args[1].capitalize())
	year = int(args[2])
else:
	print("Please enter your date in the format month [year]")
calendar.prmonth(year, month)