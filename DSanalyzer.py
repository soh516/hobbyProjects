import csv
import matplotlib.pyplot as plt
import datetime as dt

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
plt.plot(x, y)
plt.xlabel('Date (Year - Month)')
plt.ylabel('Block usage (TB)')
plt.title('DataStore')
plt.xticks(rotation=45)
plt.grid(True)
ax = plt.gca()
ax.grid(which='major', color='#DDDDDD', linestyle='dotted', linewidth=0.8)  # Major grid lines
plt.show()
