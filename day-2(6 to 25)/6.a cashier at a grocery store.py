prices = [10.0, 15.0, 30.0]  
quantities = [2, 1, 3]       
discount_rate = 0.1          
tax_rate = 0.08              

subtotal = sum(price * quantity for price, quantity in zip(prices, quantities))

discounted_subtotal = subtotal - (subtotal * discount_rate)

tax_amount = discounted_subtotal * tax_rate

total_cost = discounted_subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discounted Subtotal: ${discounted_subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
