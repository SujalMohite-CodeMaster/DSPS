# Data visualization / Exploatory Data analysis for the selected data set using Matplotlib and Seaborn.
# Create a bar graph contigency table using any 2 variables.
import pandas as pd 
import matplotlib.pyplot as plt

dataset = {
    #here I use Marks And Friends as a 2 variables.
     "Marks" : [87,86,87,87,96,94,88,88,90],
     "Friends" : ["Sujal","yash","Chandan","Harsh","Suyash","Nikhil","Chinmay","Sarthak","Paresh"]
}
# creating dataframe of the dataset
df = pd.DataFrame(dataset)

print(df)

#plotting the bar graph using the Friends and Marks
plt.bar(df["Friends"],df["Marks"])
plt.xlabel("Friends")
plt.ylabel("Marks")
plt.title("Marks of Friends")

plt.show()
