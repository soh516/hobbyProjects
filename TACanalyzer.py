import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

x_tmp = []
y_tmp = []
y2_tmp = []

with open('TAC.csv', 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    # Escape header
    header = next(csvread)
    for row in csvread:
        # only read to list if it is NOT empty
        if row[0]:
            x_tmp.append(row[0])  # Assuming the x-values are in the first column
        if row[1]:
            y_tmp.append(row[1])  # Assuming the y-values are in the second column
        if row[3]:
            y2_tmp.append(row[3])  # Assuming the y2-values are in the forth column

# Convert a string list to float list
y = list(map(float, y_tmp))
y2 = list(map(float, y2_tmp))

# Convert string to datetime object 
x = [dt.datetime.strptime(tmp, '%Y-%m').date() for tmp in x_tmp]
# I can convert datetime format via code or I could do it via matplotlibs
#x = [tmp.strftime('%Y %b') for tmp in x]
#for i in range(len(x)):
#    x[i] = x[i].strftime('%Y %b') 

# Plot historical data
plt.plot(x, y, label='Research TAC ticket', marker="o", markersize=5, linestyle='dotted', color='b')
plt.plot(x, y2, label='General TAC ticket (Excluding research TAC)', marker="d", markersize=5, linestyle='dashed', color='r')
plt.title('TAC ticket')
plt.xlabel('Date')
plt.ylabel('Number of tickets')
plt.xticks(rotation=45)
plt.grid(True)
ax = plt.gca()
# Change date format via matpltlibs https://stackoverflow.com/questions/14946371/editing-the-date-formatting-of-x-axis-tick-labels
myFmt = mdates.DateFormatter("%Y %b")
ax.xaxis.set_major_formatter(myFmt)
ax.grid(which='major', color='k', linestyle='dotted', linewidth=0.8)  # Major grid lines
#ax.grid(which='minor', color='k', linestyle='dotted', linewidth=0.5)  # Minor grid lines
#ax.minorticks_on()
ax.set_ylim([0, 70])

# Plot
plt.legend()
plt.show()

