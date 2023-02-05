import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('SampleSuperstore.csv')

grouped_data = data.groupby("Sub-Category")["Sales"].sum().nlargest(7)

# Create a figure and axis
fig, ax = plt.subplots(facecolor='lightblue')

# Define custom colors
colors = ['lawngreen', 'aqua', 'silver', 'yellow', 'mediumpurple', 'orange', 'pink']

# Plot the data with custom colors
ax.pie(grouped_data, labels=grouped_data.index, colors=colors, autopct='%1.1f%%', pctdistance=0.6)

# Set title
ax.set_title("Pie Chart")

# Show plot
plt.show()
