import matplotlib.pyplot as plt

# Sample sales data
days = list(range(1, 31))  # Days in a month (1 to 30)
sales = [150, 180, 170, 160, 190, 210, 230, 220, 240, 260, 280, 250, 270, 300, 290, 310, 330, 350, 340, 320, 310, 300, 330, 360, 380, 390, 400, 410, 420, 430]

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Line plot
ax1.plot(days, sales, marker='o', color='blue')
ax1.set_title('Line Plot: Sales Over Time')
ax1.set_xlabel('Day')
ax1.set_ylabel('Sales')

# Scatter plot
ax2.scatter(days, sales, color='green')
ax2.set_title('Scatter Plot: Sales Over Time')
ax2.set_xlabel('Day')
ax2.set_ylabel('Sales')

# Bar plot
ax3.bar(days, sales, color='orange')
ax3.set_title('Bar Plot: Sales Over Time')
ax3.set_xlabel('Day')
ax3.set_ylabel('Sales')

# Display all plots
plt.tight_layout()
plt.show()
