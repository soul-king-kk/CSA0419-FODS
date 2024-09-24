import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [3000, 3500, 3200, 4000, 4500, 4200, 4700, 5000, 4800, 5300, 4900, 5500]

# Create figure with two subplots (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Line plot
ax1.plot(months, sales, marker='o', linestyle='-', color='b')
ax1.set_title('Monthly Sales Trend')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')
ax1.grid(True)

# Bar plot
ax2.bar(months, sales, color='skyblue')
ax2.set_title('Monthly Sales Distribution')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')

# Show both plots
plt.tight_layout()
plt.show()
