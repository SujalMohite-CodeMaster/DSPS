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
    
 #outerliers are the values which is below the lower_outlier and values above the upper_outerlier
    lower_outerlier = Q1 - 1.5 *IQR # to find lower outerlier
    upper_outerlier = Q3 + 1.5 *IQR # to find upper outerlier

    outerlier = df[(df[col_name] < lower_outerlier) | (df[col_name] > upper_outerlier)]
    return outerlier 

outerlier_in_marks = outerliers(df,"Marks")
print(f"The outerlier in marks is\n{outerlier_in_marks}") 
 # Here is the only value "96" are the above upper_outerlier and none of the value is below the lower_outerlier.