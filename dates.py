# Program that determines days between dates

def isLeapYear(year):
""" determines if year is a leap year according to wikipedia rules """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
        
def monthDays(month,year):
""" 30 days hath september, april, june and november. To all the rest, 31. Except that stupid month February"""
    if month in (4,6,9,11):
        days = 30
    else:
        if month in (1,3,5,7,8,10,12):
            days = 31
        else:
            if isLeapYear(year) == True:
                days = 29
            else:
                days = 28
    return days


def nextDay(year,month,day):
""" mechanically counts the next day """
    if day < monthDays(month,year):
        return year, month, day +1
    else:
        if month == 12:
            return year +1, 1, 1
        else:
            return year, month +1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
