from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nThe current date and time is ", now)

print("\n Date components", today.year, today.month, today.day)