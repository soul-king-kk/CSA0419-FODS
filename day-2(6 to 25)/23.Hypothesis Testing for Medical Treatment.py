import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(42)
control_group = np.random.normal(loc=5, scale=1, size=100)
treatment_group = np.random.normal(loc=5.5, scale=1, size=100)
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)
plt.figure(figsize=(10, 6))
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.title('Treatment Effect Comparison')
plt.ylabel('Outcome Measure')
plt.text(1.5, plt.ylim()[1], f'p-value: {p_value:.4f}', 
         horizontalalignment='center', verticalalignment='top')
if p_value < 0.05:
    plt.text(1.5, plt.ylim()[1] - 0.1, 'Significant', 
             horizontalalignment='center', verticalalignment='top', 
             color='red', fontweight='bold')
plt.show()
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("The treatment has a statistically significant effect.")
else:
    print("There is no statistically significant effect of the treatment.")
