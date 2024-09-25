import numpy as np
import scipy.stats as stats
drug_group = [120, 115, 130, 125, 110, 140, 135, 128, 119, 122, 113, 118, 115, 121, 117]  # Example blood pressure reductions
placebo_group = [130, 132, 129, 128, 135, 138, 131, 134, 137, 136, 140, 139, 141, 142, 133]
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    std_err = stats.sem(data)
    h = std_err * stats.t.ppf((1 + confidence) / 2, len(data) - 1)
    return mean - h, mean + h
drug_ci = confidence_interval(drug_group)
placebo_ci = confidence_interval(placebo_group)
print(f"95% Confidence Interval for Drug Group: {drug_ci}")
print(f"95% Confidence Interval for Placebo Group: {placebo_ci}")
