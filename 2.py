import numpy as np

# Example sales data for 3 products
# Each row represents a product and columns represent [quantity sold, price per unit]
sales_data = np.array([[10, 15],   # Product 1: 10 units sold at $15 each
                       [5, 20],    # Product 2: 5 units sold at $20 each
                       [8, 25]])   # Product 3: 8 units sold at $25 each

# Calculate total revenue for each product
total_revenue = sales_data[:, 0] * sales_data[:, 1]  # Quantity sold * Price per unit

# Calculate the average price across all products sold
average_price = np.mean(total_revenue) / np.sum(sales_data[:, 0])  # Total revenue / total quantity sold

print(f'The average price of all products sold in the past month is: ${average_price:.2f}')
