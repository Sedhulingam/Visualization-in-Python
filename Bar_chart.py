import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('SampleSuperstore.csv')

# Aggregate the sales data at the Sub-Category level
agg_data = data.groupby('Sub-Category').Sales.sum().reset_index()

fig, ax = plt.subplots(figsize=(16,9))

# Bar chart with Sub-Category against aggregated sales
ax.barh(agg_data['Sub-Category'], agg_data['Sales'], color='maroon')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

# Data Annation
for i in ax.containers:
    for rect in i:
        width = rect.get_width()
        ax.annotate(f"{width:.2f}",
                    xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left', va='center')

ax.set_title("Bar Chart",loc='left',)

ax.invert_yaxis()
 
# Setting the X and Y labels
plt.ylabel('Sub Category')
plt.xlabel('Sales')
 
# Adding the legends
plt.show()
