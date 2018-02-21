import datetime
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

twelve_months   = date.today() - relativedelta(months=+12)

print twelve_months

eighteen_months   = date.today() - relativedelta(months=+18)

print eighteen_months