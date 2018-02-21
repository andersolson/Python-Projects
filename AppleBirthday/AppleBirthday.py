import datetime

adoptiondate = datetime.date(2016, 2, 14)

birthDate    = adoptiondate - datetime.timedelta(547) #Apple was already 1.5 years old or 547 days old

print "Apple's adoption date is {}".format(adoptiondate)
print "Apple's birthday is {}".format(birthDate)