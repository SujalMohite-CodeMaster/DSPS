import pandas as pd
import numpy as np

dataset = {
    "Friends" : ["Sujal","yash","Chandan","Harsh","Suyash","Nikhil","Chinmay","Sarthak","Paresh"],
    "Marks" : [87,86,87,87,96,94,88,88,90],
    "Address":["Dombivali","Kalwa","Kandivali","Dombivali","Dombivali","Curry Road","Bhandup","Kalwa","Asangaon"]
}

df = pd.DataFrame(dataset)
print(df)

# Adding index filed it will create column of row numbers.
df["IndexFilld"] = np.arange(len(df))
print(df)