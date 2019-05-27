# working with time

import time
import calendar

#Ticks
var1 = time.time() # gives back time from 12:00 1.1.1970
print(var1)

local = time.localtime(time.time())
print(local)

timeLocal = time.asctime(time.localtime(time.time()))
print(timeLocal)

# calendars

calendarVar = calendar.month(2019,1)
print(calendarVar)

# link for more: https://docs.python.org/3/library/datetime.html