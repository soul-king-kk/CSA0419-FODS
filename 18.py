import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Data from the image
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
age_stats = df['age'].agg(['mean', 'median', 'std'])
fat_stats = df['%fat'].agg(['mean', 'median', 'std'])

print("Age Statistics:\n", age_stats)
print("\n%Fat Statistics:\n", fat_stats)

# Boxplots for age and %fat
plt.figure(figsize=(12, 5))

# Boxplot for age
plt.subplot(1, 2, 1)
sns.boxplot(y='age', data=df)
plt.title('Boxplot of Age')

# Boxplot for %fat
plt.subplot(1, 2, 2)
sns.boxplot(y='%fat', data=df)
plt.title('Boxplot of %Fat')

plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(6, 5))
sns.scatterplot(x='age', y='%fat', data=df)
plt.title('Scatter plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.show()

# Q-Q plots
plt.figure(figsize=(12, 5))

# Q-Q plot for age
plt.subplot(1, 2, 1)
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q plot for Age')

# Q-Q plot for %fat
plt.subplot(1, 2, 2)
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title('Q-Q plot for %Fat')

plt.tight_layout()
plt.show()
