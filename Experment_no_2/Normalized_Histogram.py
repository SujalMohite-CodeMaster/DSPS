# Creating a normalized histogram of the data set using Matplotlib and Seaborn.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataset = {
    "GPA" : [5.5,5.6,5.7,5.8,6.0,6.4,6.8,6.7,6.9,7.0,7.5,7.7,7.8,8.0,8.2,8.4,8.5,8.8,9.0,9.4,9.6,9.8],
    "Alphabets" :["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]

}

df = pd.DataFrame(dataset)

print(df)

sns.histplot(df["GPA"],kde=True,stat="density",bins=10) #stat="density" is used to normalize the histogram
plt.xlabel("GPA")
plt.ylabel("Density")
plt.title("Normalized Histogram of GPA")


plt.show()