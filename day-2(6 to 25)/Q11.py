import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [100, 200, 150, 300]
plt.plot(months, sales)
plt.title('Product Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
plt.scatter(months, sales)
plt.title('Product Sales Over Time (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
plt.bar(months, sales)
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
