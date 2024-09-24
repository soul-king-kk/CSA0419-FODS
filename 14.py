import pandas as pd
from collections import Counter

# Sample data representing customer purchases
data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'age': [25, 30, 25, 35, 40, 30, 25, 40],  # Ages of customers
    'purchase_amount': [200, 150, 250, 100, 300, 120, 500, 130]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Extract the 'age' column
ages = df['age']

# Calculate the frequency distribution of ages
age_distribution = Counter(ages)

# Display the frequency distribution
for age, freq in age_distribution.items():
    print(f'Age {age}: {freq} customers')
