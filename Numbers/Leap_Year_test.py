
# ! Check LeapYear
def isYearLeap(year):

    return bool((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

# ! End of Month Check
def daysInMonth(year, month):

    if isYearLeap(year) and month == 2:
        return 29
    if month == 2:
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31


def dayOfYear(year, month, day):
    daysinPriorMonth = 0

    for i in range(month, 1, -1):
        daysinPriorMonth += daysInMonth(year, i-1)

    return daysinPriorMonth + day


print(dayOfYear(2000, 12, 31))