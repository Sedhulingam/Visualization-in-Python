import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('SampleSuperstore.csv')

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.scatter(data['Sales'],data['Profit'],color="black",marker="*")

ax.set_facecolor("aqua")

# Set title and labels
ax.set_title("Scatter Plot")
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")

# Show plot
plt.show()
