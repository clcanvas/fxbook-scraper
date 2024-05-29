# Notice
This is an old project I made a long time ago that I thought I would add to GitHub

# Introduction
This project takes data from myfxbook.com and presents the economic calender for the current date.
This program potential for use in automated trend analyzation, prediction, comparison, etc.
Right now, the results are simply printed to the console, but modifications can be made for data to be added to text files, saved to spreadsheet files, etc.

# How to Use
I am running this through a virtual environment, but have provided a requirements.txt that has all the required libraries and packages you will need
To change any of the settings, you will need to edit the variables in the script.
To use the program, set your options in main.py and run main.py. 

For example, to run the program every day at 11:05 PM in the Eastern US Timezone:

```
TIMEZONE = "(GMT -4:00) Atlantic Time (Canada), La Paz, Santiago, Georgetown, Caracas";
TARGET_HOUR=23
TARGET_MINUTE=5
TARGET_SECOND=0
INSTANT = False
```

Keep in mind, the instant variable indicates whether the website will be checked the moment the program is run if set to true or run everyday at a specific time when set to false.