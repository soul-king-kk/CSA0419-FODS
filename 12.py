import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [5, 7, 10, 15, 20, 25, 30, 28, 22, 18, 10, 6]
rainfall = [78, 60, 65, 50, 40, 20, 15, 18, 35, 55, 70, 80]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Line plot for temperature
ax1.plot(months, temperature, marker='o', color='red', linestyle='-')
ax1.set_title('Monthly Temperature Data')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

# Scatter plot for rainfall
ax2.scatter(months, rainfall, color='blue')
ax2.set_title('Monthly Rainfall Data')
ax2.set_xlabel('Month')
ax2.set_ylabel('Rainfall (mm)')

# Display both plots
plt.tight_layout()
plt.show()
