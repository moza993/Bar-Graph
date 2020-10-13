import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import csv


#First select file csv path with data (this replaces 'C:\Your data'), give each data column a name, you can add or remove columns as you wish:
data = pd.read_csv(r'C:\Your data', header = 0, usecols = ['column 1', 'column 2', 'column 3', 'column 4'] ) 
df = pd.DataFrame(data)


#Now choose the column titles to display on the graph, N is the number of bars that will displayed and should be changed accordingly
N = 4 
column_1 = df['column 1'].tolist()
column_2 = df['column 2'].tolist()
column_3 = df['column 3'].tolist()
column_4 = df['column 4'].tolist()

ind = np.arange(N) 


#You can also change the width of the bar
width = 0.2


plt.bar(ind, column_1, width, label='column 1')
plt.bar(ind + width, column_2, width, label='column 2')
plt.bar(ind + 2*width, column_3, width, label='column 3')
plt.bar(ind + 3*width, column_4, width, label='column 4')

labels = (i for i in range(1, N+1))

#Y axis label
plt.ylabel('Y axis')

#X axis label
plt.xlabel('X axis')
plt.xticks(ind + width*1.5, labels)
plt.legend(loc = 'best')
plt.show()


