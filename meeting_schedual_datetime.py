""" function that determines which day of the month a meetup should be held. 
the meeting is on the a  specific weekday of a nth weeks of a month (they are optional argument) . 
The function should accept year and month, weekday and the the number of the week in a month arguments and 
should return a datetime.date object representing the day of the month for the meetup. The weekday  either represented by number of by weekday name of it (MONDAY = 0
    TUESDAY = 1
    WEEDENSDAY = 2
    THURSDAY = 3
    FRIDAY = 4 
    SATURDAY = 5 
    SUNDAY = 6)
    Also nth can be negative indicating the number of the week from end of the end.
"""

import calendar
from enum import Enum, unique
import datetime
class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEEDENSDAY = 2
    THURSDAY = 3
    FRIDAY = 4 
    SATURDAY = 5 
    SUNDAY = 6
     
    
def meetup_date(year,month, nth=4, weekday=3):
    c= calendar.monthcalendar(year,month)
    # print(c)
    w = weekday if isinstance(weekday, int)  else weekday.value
    if nth> 0:
        nth_week = c[nth-1] if c[0][w] != 0 else c[nth]
            
    else:
        nth_week = c[nth-1] if c[-1][w] == 0 else c[nth]
        print(nth_week)
    meeting_day_date = nth_week[w]
    meeting_date = datetime.date(year = year,month = month, day = meeting_day_date )
    return meeting_date
