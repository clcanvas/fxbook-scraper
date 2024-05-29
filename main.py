from datetime import date, datetime
from src.fxbookutils.site_data import *
import os

# User Options
TIMEZONE = "(GMT -4:00) Atlantic Time (Canada), La Paz, Santiago, Georgetown, Caracas"; # go to the website and copy the exact text for your timezone and put it here
# Single digit times will only accept one digit ie. TARGET_MINUTE=5
TARGET_HOUR=23 # ##:00:00 | 24-hour time
TARGET_MINUTE=5 # 00:##:00
TARGET_SECOND=0 # 00:00:##
INSTANT = False  # True : will grab data when the script is run | False : Will grab based on target times (e.g. if target hour is 23, minute 5, and second 0 scrpt will run at 23:05:03 or 11:05:00 PM)

URL = "https://www.myfxbook.com/forex-economic-calendar" # url to check 


def printRows(calRows):
    day = str(date.today())[8:10]
    print(f"Economic Calender on {date.today()}")
    for row in calRows:
        if row.dataRowID != None and row.name != None:
            if row.day[4:6] == day:
                print(row)
            else:
                break
    os.remove("fxbook.html")

if not INSTANT:
    print(f"Site will be scraped at: {TARGET_HOUR}:{TARGET_MINUTE if TARGET_MINUTE >= 10 else f'0{TARGET_MINUTE}'}:{TARGET_SECOND if TARGET_SECOND >= 10 else f'0{TARGET_SECOND}'}")
    while True:
        target_time = datetime.now().replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=TARGET_SECOND, microsecond=0)
        current_time = datetime.now().time()
        if current_time.hour == target_time.hour and current_time.minute == target_time.minute and current_time.second == target_time.second:
            printRows(getRowsFromSite(URL, TIMEZONE))
else:
    print("Running instantly")
    printRows(getRowsFromSite(URL, TIMEZONE))
