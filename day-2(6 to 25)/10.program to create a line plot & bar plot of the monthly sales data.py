import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1500, 1800, 2100, 2500, 3000, 3500, 3700, 3200, 3100, 3300, 3600, 4000]

plt.figure(figsize=(14, 6))

# 1. Line Plot
plt.subplot(1, 2, 1)  # (1 row, 2 columns, 1st plot)
plt.plot(months, sales, marker='o', color='b', linestyle='-', linewidth=2)
plt.title('Monthly Sales Data (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)

# 2. Bar Plot
plt.subplot(1, 2, 2)  # (1 row, 2 columns, 2nd plot)
plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales Data (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.tight_layout()  
plt.show()
