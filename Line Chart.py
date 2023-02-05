import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('SampleSuperstore.csv')

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(data['Sales'],data['Profit'])

# Set title and labels
ax.set_title("Line Chart")
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")

# Show plot
plt.show()
