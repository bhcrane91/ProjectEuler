"""
You are given the following information, but you may prefer 
to do some research for yourself.

- 1 Jan 1900 was a Monday.
- 28 / 29 days: February / leap year
- 30 days: September, April, June and November.
- 31 days: January, March, May, July, August, October, December

A leap year occurs on any year evenly divisible by 4, but not on
a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import numpy as np

# 2: 28 | 2: 29 if year % 4 == 0 and year % 400 == 0
# 30: 4, 6, 9, 11
# 31: 1, 3, 5, 7, 8, 10, 12
# Weekdays Sun:7 Mon:1 Tues:2 Wed:3 Thur:4 Fri:5 Sat:6

"""
months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30, 
    10: 31,
    11: 30,
    12: 31
}

week = np.array([1,2,3,4,5,6,7])
all_days = np.tile(week,36889//7)

remainder = 36889 % 7
if remainder > 0:
    all_days = np.concatenate((all_days, week[:remainder]))
    
zeros = np.zeros((36889,4),dtype=int)
zeros[:,0] = all_days
print(zeros)
zeros[0] = np.array([1,1,1,1900])
print(zeros)
for i in zeros[1:]:
    new_day = np.array([zeros[i-1][0],0,0,0])
    last_day = zeros[i-1][1]
    last_mon = zeros[i-1][2]
    if last_mon == 12 and last_day == 31:
""" 

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30, 
    10: 31,
    11: 30,
    12: 31
}

weekday = 1
day = 1 
month = 1    
year = 1900
date = [weekday,day,month,year]
start_date = [1,1,1901]
end_date = [31,12,2000]
count_on = False
which = 0
count_weekday = 0
while date[1:] != end_date:
    if date[1:] == start_date:
        count_on = True 

    if count_on and weekday == which and day == 1:
        count_weekday += 1

    # print(date)
    # Leap Year
    if month == 2 and day == 1:
        if (year % 4 == 0  and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            months[month] = 29 
        else:
            months[month] = 28
    # Next Day
    if months[month] == day:
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        day = 1
    else: 
        day += 1 
    weekday = (weekday+1) % 7
    date = [weekday,day,month,year]
    
print(count_weekday)