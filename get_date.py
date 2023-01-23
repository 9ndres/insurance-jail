from datetime import date, datetime

current_date = date.today()
slash_date = current_date.strftime("%d/%m/%Y")
day = current_date.strftime('%d')
month = current_date.strftime('%m')
year = current_date.strftime('%Y')
hour = datetime.now()
str_date = hour.strftime("%H : %M")
