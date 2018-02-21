#import datetime
#from datetime import date, datetime

#now = date.today()

#print("Today: {}".format(now))

#bd_y = 1985
#bd_m = 6
#bd_d = 24

#age = date(int(bd_y), int(bd_m), int(bd_d))

#print("Age is: {}".format(now-age))

#delta = datetime.now() - datetime(1985, 5, 8)
#print "Your age is %d months" % (delta.days)

#dob = datetime.strptime('07-30-1950', '%m-%d-%Y')
#now = datetime.now()
#years = now.year - dob.year
#months = now.month - dob.month

#print(months)

#if now.day < dob.day:
    #months -= 1
#while months < 0:
    #months += 12
    #years -= 1
#age = '{}y{}mo'.format(years, months)

#print age

import time
from datetime import date
today = date.today()
print(today)

today == date.fromtimestamp(time.time())

my_birthday = date(2017, 6, 24)

time_to_birthday = abs(today - my_birthday)

print(time_to_birthday.days)