import pandas as pd
import numpy as np

dataset = {
    "Friends" : ["Sujal","yash","Chandan","Harsh","Suyash","Nikhil","Chinmay","Sarthak","Paresh"],
    "Marks" : [87,86,87,87,96,94,88,88,90],
    "Address":["Dombivali","Kalwa","Kandivali","Dombivali","Dombivali","Curry Road","Bhandup","Kalwa","Asangaon"]
}
df = pd.DataFrame(dataset)

print(df)

def outerliers(df,col_name):
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)

    IQR = Q3 -Q1
    print(IQR)

    lower_outerlier = Q1 - 1.5 *IQR
    upper_outerlier = Q3 + 1.5 *IQR

    outerlier = df[(df[col_name] < lower_outerlier) | (df[col_name] > upper_outerlier)]
    return outerlier , IQR

outerlier_in_marks = outerliers(df,"Marks")
print(f"The outerlier in marks is\n{outerlier_in_marks}")