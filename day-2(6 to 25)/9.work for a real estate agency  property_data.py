import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5, 6],
    'location': ['Downtown', 'Suburbs', 'Downtown', 'Suburbs', 'Countryside', 'Downtown'],
    'bedrooms': [3, 5, 2, 4, 6, 5],
    'area_sqft': [1500, 2500, 1200, 1800, 3000, 2200],
    'listing_price': [500000, 750000, 400000, 600000, 850000, 700000]
}

property_data = pd.DataFrame(data)

average_price = property_data.groupby('location')['listing_price'].mean()
print("Average price in each location:\n", average_price)

properties_count = property_data[property_data['bedrooms'] > 4].shape[0]
print("\nNumber of properties with more than 4 bedrooms:", properties_count)

largest_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nProperty with the largest area:\n", largest_property)
