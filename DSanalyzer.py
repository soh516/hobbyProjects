import csv
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

x_tmp = []
y_tmp = []

with open('DS.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x_tmp.append(row[0])  # Assuming the x-values are in the first column
        y_tmp.append(row[1])  # Assuming the y-values are in the second column

y = list(map(float, y_tmp))
y[:] = [tmp / 1000 for tmp in y]
x = [dt.datetime.strptime(tmp, '%m/%d/%Y').date() for tmp in x_tmp]
plt.plot(x, y, label='Historical')
plt.xlabel('Date (Year)')
plt.ylabel('Block usage (PB)')
plt.title('DataStore')
plt.xticks(rotation=45)
plt.grid(True)
ax = plt.gca()
ax.grid(which='major', color='#DDDDDD', linestyle='dotted', linewidth=0.8)  # Major grid lines
ax.grid(which='minor', color='#EEEEEE', linestyle='dotted', linewidth=0.8)  # Major grid lines
ax.minorticks_on()

date_range = list(range(1, len(y)+1))
date_range_reshaped = np.array(date_range).reshape(-1, 1)
model = LinearRegression()
model.fit(date_range_reshaped, y)
prediction_days = 2400
future_dates = pd.date_range(start='2024-04-30', periods=prediction_days, freq='D')
x_numeric = list(range(len(y)+1, len(y)+prediction_days+1))
x_numeric_reshaped = np.array(x_numeric).reshape(-1, 1)
y_predict = model.predict(x_numeric_reshaped)
plt.plot(future_dates, y_predict, label='Predictions', color='r')
#print(future_dates[1])
vx = dt.datetime.strptime('01/01/2027', '%m/%d/%Y').date()
plt.vlines(x = vx, ymin = 0, ymax = max(y_predict), colors = 'purple', linestyle = 'dotted')
vy_xmin = dt.datetime.strptime('01/01/2029', '%m/%d/%Y').date()
vy_xmax = dt.datetime.strptime('12/01/2030', '%m/%d/%Y').date()
plt.hlines(xmin = vy_xmin, xmax= vy_xmax, y = 2.4, colors = 'purple', linestyle = 'dotted')
plt.plot(vx, 1.7965, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
vx1 = dt.datetime.strptime('04/14/2030', '%m/%d/%Y').date()
plt.plot(vx1, 2.4, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.text(vx, 1.7, '(01/01/2027, 1.799)')
plt.text(vx1, 2.3, '(04/14/2030, 2.4)')
plt.legend()
plt.show()
