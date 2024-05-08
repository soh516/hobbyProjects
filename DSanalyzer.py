import csv
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

x_tmp = []
y_tmp = []

with open('DS3.csv', 'r') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    # Escape header
    header = next(csvread)
    for row in csvread:
        if row[0]:
            x_tmp.append(row[0])  # Assuming the x-values are in the first column
        if row[1]:
            y_tmp.append(row[1])  # Assuming the y-values are in the second column

# Convert a string list to float list
y = list(map(float, y_tmp))

# Convert TB to PB. This would reuse the list y. 
y[:] = [tmp / 1000 for tmp in y]

# Convert string to datetime object 
x = [dt.datetime.strptime(tmp, '%m/%d/%Y').date() for tmp in x_tmp]

# Plot historical data
plt.plot(x, y, label='Historical')
plt.xlabel('Date')
plt.ylabel('Block usage (PB)')
plt.title('DataStore')
plt.xticks(rotation=45)
plt.grid(True)
ax = plt.gca()
ax.grid(which='major', color='#DDDDDD', linestyle='dotted', linewidth=0.8)  # Major grid lines
ax.grid(which='minor', color='#EEEEEE', linestyle='dotted', linewidth=0.5)  # Minor grid lines
ax.minorticks_on()

# Get the last day of the historical data
last_his_date = x_tmp[-1]
# Last day plus 1 --> first prediction date
first_prediction_date = dt.datetime.strptime(last_his_date, '%m/%d/%Y').date() + dt.timedelta(days=1)

# Model with historical data
date_range = list(range(1, len(y)+1))
date_range_reshaped = np.array(date_range).reshape(-1, 1)
model = LinearRegression()
model.fit(date_range_reshaped, y)

# Predict future with historical data
prediction_days = 2400
future_dates = pd.date_range(start=first_prediction_date, periods=prediction_days, freq='D')
x_numeric = list(range(len(y)+1, len(y)+prediction_days+1))
x_numeric_reshaped = np.array(x_numeric).reshape(-1, 1)
y_predict = model.predict(x_numeric_reshaped)

# Plot future data
plt.plot(future_dates, y_predict, label='Predictions', color='r')

# Points of interest with a specific date 
date_of_interest = '01/01/2027'
future_dates_str = future_dates.strftime('%m/%d/%Y')
index1 = 0
while index1 < len(future_dates_str) and future_dates_str[index1] != date_of_interest:
        index1 = index1 + 1
vx = dt.datetime.strptime(date_of_interest, '%m/%d/%Y').date()
plt.text(vx, round(y_predict[index1], 1), '(' + date_of_interest + ', ' + str(round(y_predict[index1], 3)) +')')
plt.plot(vx, y_predict[index1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")

# Points of interest with a specific value
vaule_of_interest = 2.4
index2 = 0
while index2 < len(y_predict) and abs(y_predict[index2] - vaule_of_interest) > 0.0005:
        index2 = index2 + 1
vx1 = dt.datetime.strptime(future_dates_str[index2], '%m/%d/%Y').date()
plt.plot(vx1, vaule_of_interest, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.text(vx1, vaule_of_interest, '(' + future_dates_str[index2] + ', ' +  str(vaule_of_interest) + ')')

# Plot
plt.legend()
plt.show()
