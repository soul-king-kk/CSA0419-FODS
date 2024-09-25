import pandas as pd
data = {
    'product_name': ['Laptop', 'Smartphone', 'Headphones', 'Laptop', 'Smartwatch',
                     'Smartphone', 'Laptop', 'Headphones', 'Smartphone', 'Smartwatch'],
    'order_quantity': [5, 8, 10, 3, 4, 6, 7, 15, 9, 5]
}
sales_data = pd.DataFrame(data)

total_sales_per_product = sales_data.groupby('product_name')['order_quantity'].sum()

sorted_sales = total_sales_per_product.sort_values(ascending=False)

top_5_products = sorted_sales.head(5)

print("Top 5 products sold the most in the past month:\n", top_5_products)
