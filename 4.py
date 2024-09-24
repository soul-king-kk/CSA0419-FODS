import numpy as np

# Example sales_data array (quarters: [Q1, Q2, Q3, Q4])
sales_data = np.array([150000, 200000, 250000, 300000])

# Calculate total sales for the year
total_sales = np.sum(sales_data)

# Calculate the percentage increase from Q1 to Q4
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]
percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100

# Print the results
print("Total sales for the year:", total_sales)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase)
