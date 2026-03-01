# this programs accepts a century from 1 to 100 (inclusive) and prints
# all those years of that century which  have exactly three Friday the 13th's

import datetime

century = int(input("Please Enter a Century between 1 and 100: "))

def isLeapYear(year):
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0 and not year % 100 == 0):
        return True
    return False

for year in range(1, 101):
   
    curr_year = min((century - 1) * 100 + year, 9999)
    curr_date  = datetime.date(curr_year, 1, 1)

    unlucky = 0

    if (isLeapYear(curr_year)):
        if (curr_date.weekday() == 6):
            unlucky = 1
    else:
        if (curr_date.weekday() == 3):
            unlucky = 1

    if (unlucky):
         print(curr_date.strftime('%Y'))
