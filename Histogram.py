import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,4, 5, 5, 5, 5, 5,6,6,6,6,7,7,7,8,8,9]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.hist(data, bins=9,color='lightgreen')

# Set title and labels
ax.set_title("Histogram")
ax.set_xlabel("Values")
ax.set_ylabel("Frequency")

# Show plot
plt.show()
