from datetime import date,timedelta,datetime

time = datetime.now()
seconds = time.strftime("%Y-%m-%d, %H:%M:%S")
print(seconds)