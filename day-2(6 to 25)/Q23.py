import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'treatment': [10, 12, 14, 10, 13, 15],
    'placebo': [12, 14, 15, 11, 13, 14]
})
treatment_group = data['treatment']
placebo_group = data['placebo']
t_stat, p_value = stats.ttest_ind(treatment_group, placebo_group)
plt.boxplot([treatment_group, placebo_group], labels=['Treatment', 'Placebo'])
plt.title('Effectiveness of New Treatment vs Placebo')
plt.ylabel('Blood Pressure Reduction')
plt.show()
print(f"P-value from hypothesis testing: {p_value}")
