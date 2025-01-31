import pandas as pd
import numpy as np

dataset = {
     "Marks" : [87,86,87,87,96,94,88,88,90]
}

print(dataset)

df = pd.DataFrame(dataset)

print(df)

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IOR = Q3 - Q1

lower_outerlier = Q1 - 1.5 * IOR
upper_outerlier = Q3 + 1.5 * IOR

print(lower_outerlier,upper_outerlier)

print(f"Q1 is {Q1} and Q2 is {Q3}")
print("IOR is ",IOR)