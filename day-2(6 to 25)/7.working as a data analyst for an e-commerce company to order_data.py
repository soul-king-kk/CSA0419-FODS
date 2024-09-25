import pandas as pd
data = {
    'customer_id': [101, 102, 103, 102, 104, 101],
    'order_date': ['2023-01-15', '2023-02-10',  '2023-01-20', '2023-03-15', '2023-04-10', '2023-05-25'],
    'product_name': ['Apple', 'Banana', 'Carrot', 'Banana', 'Apple', 'Carrot'],
    'order_quantity': [3, 5, 4, 3, 1, 6]
}

order_data = pd.DataFrame(data)

total_orders_per_customer = order_data['customer_id'].value_counts()
print("Total number of orders made by each customer:\n", total_orders_per_customer)

average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("\nAverage order quantity for each product:\n", average_order_quantity_per_product)

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
