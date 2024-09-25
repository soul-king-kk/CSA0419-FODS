import pandas as pd
customer_data = pd.DataFrame({
    'age': [25, 30, 25, 40, 30, 25]
})
age_distribution = customer_data['age'].value_counts()
print("Frequency Distribution of Customer Ages:\n", age_distribution)
