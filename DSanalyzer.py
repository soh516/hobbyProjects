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
plt.ylabel('Block usage (TB)')
plt.title('DataStore')
plt.xticks(rotation=45)
plt.grid(True)
ax = plt.gca()
ax.grid(which='major', color='#DDDDDD', linestyle='dotted', linewidth=0.8)  # Major grid lines

date_range = list(range(1, len(y)+1))
date_range_reshaped = np.array(date_range).reshape(-1, 1)
model = LinearRegression()
model.fit(date_range_reshaped, y)
future_dates = pd.date_range(start='2024-04-30', periods=1500, freq='D')
x_numeric = list(range(len(y)+2, len(y)+1500+2))
x_numeric_reshaped = np.array(x_numeric).reshape(-1, 1)
y_predict = model.predict(x_numeric_reshaped)
plt.plot(future_dates, y_predict, label='Predictions', color='r')
plt.legend()
plt.show()
