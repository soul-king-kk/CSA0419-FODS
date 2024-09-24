import numpy as np

# Assume house_data is already imported as a NumPy array
# Example structure of house_data: 
# Each row represents a house, columns: [bedrooms, square_footage, sale_price]
house_data = np.array([[3, 1500, 300000],   # House 1
                       [5, 2000, 450000],   # House 2
                       [4, 1800, 350000],   # House 3
                       [6, 2200, 600000],   # House 4
                       [7, 2500, 700000]])  # House 5

# Filter the houses with more than 4 bedrooms
houses_with_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]

# Check if there are any houses that meet the criteria
if houses_with_more_than_four_bedrooms.size > 0:
    # Calculate the average sale price for these houses
    average_sale_price = np.mean(houses_with_more_than_four_bedrooms[:, 2])  # Column index 2 is sale price
    print(f'The average sale price of houses with more than four bedrooms is: ${average_sale_price:.2f}')
else:
    print('No houses with more than four bedrooms found.')
