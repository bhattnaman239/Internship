#date and time
print("\nDATE AND TIME\n")
from datetime import timezone, datetime, timedelta
now=datetime.now()
print(f"Current Date and Time: {datetime.now()}")
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time (till seconds): {formatted_time}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")

now = datetime.now()
updated = now.replace(month=9,hour=10)
print(f"Updated Time: {updated}")
future_date = datetime.now()+ timedelta(days=10) 
future_time = datetime.now() + timedelta(hours=24)  
ten_weeks_ago = datetime.now() - timedelta(weeks=10)
print(f"10 Weeks Ago: {ten_weeks_ago}")
print(f"10 days after: {future_date}")
print(f"10 hours after: {future_time}")


#Difference between two dates
print("\nDIFFERENCE BTW TWO DATES:")
d1 = datetime(2025, 1, 22)
d2 = datetime(2003, 8, 2)
delta = abs(d2 - d1)
print(delta.days)


# Current time in UTC
print("\nTIME ZONE:")
utc = datetime.now(timezone.utc)
print(f"Current UTC Time: {utc}")
ist = utc + timedelta(hours=5, minutes=30)
print(f"Current IST Time: {ist}")




