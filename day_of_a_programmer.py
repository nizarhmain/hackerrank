# 1700 to 2700 min and max range

# 1700 to 1917 julian calendar

# 1918 they switched

# 31st january -> 14 februrary

# 14 february is the 32th

# 1919 gregorian calendar

# feb has either 28 or 29 days

# for the julian calendar
# solstice mod 4 = 0 => use 29 otherwise use 28


# for gregorian its a bit different
# mod 400 = 0
# mod 4 = 0 && mod 100 != 0


# dd.mm.yyyy


import datetime
from datetime import timedelta

year = 1917

def is_julian_leap(year):

    main_condition = year % 4 == 0

    print(main_condition)

    dt = datetime.datetime(year, 1, 1)

    target = '' 

    # unless its the beginning of the century

    # so 1700, 1800 and 1900

    if dt.year == 1700 or year == 1800 or year == 1900:
        target = dt + timedelta(days=254)
        return target.strftime("%d.%m.%Y")

    if main_condition == False:
        target = dt + timedelta(days=254)
    else:
        target = dt + timedelta(days=255)

    return target.strftime("%d.%m.%Y")


def dayOfProgrammer(year):
    date = datetime.datetime(year, 1, 1)

    # 14 february 1918
    adoption_date = datetime.datetime(1918, 2, 14)

    difference = date - adoption_date

    # print(difference.days)

    if difference.days >= 0:
        # use gregorian
        dt = datetime.datetime(year, 1, 1)
        target = dt + timedelta(days=255)
        print(target.strftime("%d.%m.%Y"))

    else:
        # use julian
        print(is_julian_leap(year))


dayOfProgrammer(year)
