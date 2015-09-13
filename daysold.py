# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

##leap year algorithm;
##if (year is not exactly divisible by 4) then (it is a common year)
##else
##if (year is not exactly divisible by 100) then (it is a leap year)
##else
##if (year is not exactly divisible by 400) then (it is a common year)
##else (it is a leap year)

def leapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # take care of these days so I can focus on month math
    days = day2 - day1
    
    # adjusting counter to the first full month
    month2 = month2 - 1 

    # counts days in each month of current year
    while year2 >= year1:
        while month2 > 0:
            days = days + daysOfMonths[month2 - 1] # list is zero indexed (hence -1)
            if month2 == 2: # if month is February
                if leapYear(year2): # if leap year
                    days = days + 1 # feb 29th
            month2 = month2 - 1 # advance to next month
        year2 = year2 - 1 # advance to next (full) year
        if year2 == year1:
            month2 = 13 - month1
        else:
            month2 = 12

##    if True:
##        days = days + day1
##        month1 = month1 - 1
##        while month1 > 0:
##                days = days + daysOfMonths[month1 - 1] # list is zero indexed (hence -1)
##                if month1 == 2: # if month is February
##                    if leapYear(year2): # if leap year
##                        days = days + 1 # feb 29th
##                month1 = month1 - 1 # advance to next month
    return days

# Test routine

print daysBetweenDates(2012,1,1,2012,2,28)
print daysBetweenDates(2012,1,1,2012,3,1)
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2011,1,1,2012,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)

##def test():
##    test_cases = [((2012,1,1,2012,2,28), 58), 
##                  ((2012,1,1,2012,3,1), 60),
##                  ((2011,6,30,2012,6,30), 366),
##                  ((2011,1,1,2012,8,8), 585 ),
##                  ((1900,1,1,1999,12,31), 36523)]
##    for (args, answer) in test_cases:
##        result = daysBetweenDates(*args)
##        if result != answer:
##            print "Test with data:", args, "failed"
##        else:
##            print "Test case passed!"
##
##test()

## alt+3 and alt+4 block comment
