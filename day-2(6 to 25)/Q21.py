import numpy as np
import pandas as pd
import scipy.stats as stats
def confidence_interval(data, confidence):
    mean = np.mean(data)
    std_err = stats.sem(data)
    h = std_err * stats.t.ppf((1 + confidence) / 2, len(data) - 1)
    return mean - h, mean + h
file_path = "D:/Slot-D/fods/code/Q21sample.csv"  
data = pd.read_csv(file_path)
concentrations = data['concentration']  
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter the desired level of precision: "))
sample = np.random.choice(concentrations, size=sample_size)
ci = confidence_interval(sample, confidence_level)
print(f"Confidence Interval for the mean concentration: {ci}")
