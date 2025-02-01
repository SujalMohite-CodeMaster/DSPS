import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

# Load the CSV file
file_path = r"C:\Users\mohit\Python_Tutorials\Panda\Friends.csv"
df = pd.read_csv(file_path)


print("Unique cities:", df['cities'].unique())

# Define two groups
group_a = df[df['cities'] == 'Dombivali']['marks'].dropna()  
group_b = df[df['cities'] == 'Gujarat']['marks'].dropna()    


if len(group_a) == 0 or len(group_b) == 0:
    print("One of the groups is empty. Please check your group conditions.")
else:
    # Perform two-sample Z-test
    z_stat, p_value = ztest(group_a, group_b)

    print("Two-sample Z-test")
    print(f"Z-Statistic: {z_stat:.4f}")
    print(f"P-Value: {p_value:.6f}")

    
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: There is a significant difference between the two groups.")
    else:
        print("Fail to reject the null hypothesis: No significant difference between the groups.")
