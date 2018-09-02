#Q.1- Print the current day using Datetime module.

from datetime import date
import calendar

x=date.today()
print(calendar.day_name[x.weekday()])

#Q.2- Open your browser and play a video using webbrowser module in python.

import webbrowser
webbrowser.open_new_tab('https://www.youtube.com/watch?v=JjaqBsfBB-k')

#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.

import os
path='C:/Users/afroPC/Desktop/New'
files=os.listdir(path)
i=1
for file in files:
    os.rename(file, str(i)+'.jpg')
    i = i+1
