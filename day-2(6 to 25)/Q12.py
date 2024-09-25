import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr']
temperature = [30, 32, 35, 33]
rainfall = [2.5, 3.0, 1.5, 0.0]
plt.plot(months, temperature)
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()
plt.scatter(months, rainfall)
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.show()
