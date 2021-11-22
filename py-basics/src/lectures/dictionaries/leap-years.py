# 7kyu | Leap Years
# https://www.codewars.com/kata/526c7363236867513f0005ca/python


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Leap years should return True
print(isLeapYear(1984))  # Year 1984 was a leap year
print(isLeapYear(2000))  # Year 2000 was a leap year!

# Leap years should return False
print(isLeapYear(1234))  # Year 1234 was NOT a leap year!
print(isLeapYear(1100))  # Year 1100 was NOT a leap year!
