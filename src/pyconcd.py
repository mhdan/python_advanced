# pyconcd.py
# this is countdown time counter to specific constant time!
# in implemention, we consider to timezones, datetime_objects and module import!!!

from dateutil import parser, tz
from dateutil.relativedelta import relativedelta
from datetime import datetime

# with parser we parse time from string!
PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
# replace timezone with "tzinfo=tz.gettz("some timezone")"


def time_amount(time_unit: str, countdown: relativedelta) -> str:
    t = getattr(countdown, time_unit)
    # get the attribute and return the string if it wasn't zero 0 !
    return f"{t} {time_unit}" if t != 0 else ""


def main():
    # always get time in "aware" state. ("aware" means that it has speicfied timezone!!!)
    now = datetime.now(tz=tz.tzlocal())
    countdown = relativedelta(PYCON_DATE, now)
    # compute the time between 2 datetime, with "relativedelta()"
    time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
    output = (t for tu in time_units if (t := time_amount(tu, countdown)))
    # we have "walrus operator" here (form python3.8), we can use it for assign and return value at same time!!!
    # we return t if it retutn none empty string!
    # here "output" is generator object that we should iterate on it for accessing to values!!
    pycon_date_str = PYCON_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
    print(f"PyCon US 2021 will start on:", pycon_date_str)
    print("Countdown to PyCon US 2021:", ", ".join(output))


# with this line we can import it in ohters files,
# the guard clause to make sure that main() only runs when this file is executed as a script.
# This allows other people to import your code and reuse PYCON_DATE, for instance, if they’d like.
if __name__ == "__main__":
    main()

# #########################

# from dateutil import parser, tz
# from dateutil.relativedelta import relativedelta
# from datetime import datetime

# PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
# PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz('America/New_York'))

# def time_amount(time_unit: str, countdown: relativedelta) -> str:
#     t = getattr(countdown, time_unit)
#     if t != 0:
#         return f"{t} {time_unit}"
#     else:
#         return ""

# now = datetime.now(tz=tz.tzlocal())
# countdown = relativedelta(PYCON_DATE, now)
# time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
# output = []
# for tu in time_units:
#     t = time_amount(tu, countdown)
#     if t:   # checking if t is not empty, append it !
#         output.append(t)
# PYCON_DATE_str = PYCON_DATE.strftime("%A, %B %d, at %H:%M %p %Z")
# print(f"PyCon US 2021 will start on :", PYCON_DATE_str)
# print(f"Countdown to Pycon US 2021:", ", ".join(output))
