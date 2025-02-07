import pandas as pd
import numpy as np

# loading the data set
file_path = r"C:\Users\Administrator\Documents\Sujal\DSPS\car_price_dataset.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


total_records = df.shape[0]
print(f"Total number of records in the dataset: {total_records}")

print("\n")  


# View the first n rows of the DataFrame
print(df.head(n=5),"\n")

# View the last n rows of the DataFrame
print(df.tail(n=5),"\n")

# View the DataFrame info (datatypes, memory usage, etc.)
print(df.info(),"\n")

# View summary statistics of numerical columns
print(df.describe(),"\n")

# View the shape of the DataFrame (rows, columns)
print(df.shape,"\n")

# View the column names
print(df.columns,"\n")

# View the index (row labels) of the DataFrame
print(df.index,"\n")

# View data types of columns
print(df.dtypes,"\n")

# Select a single column
print(df['Brand'])

# Select multiple columns
print(df[['Model', 'Year']])

# Select a row by index position
print(df.iloc[2],"\n")

# Select rows by label index
print(df.loc[2],"\n")

# Select specific rows and columns
print(df.loc[2, 'Brand'],"\n")

# Select by condition (Boolean indexing)
print(df[df['Year'] > 5,"\n"])

# Select rows with multiple conditions
print(df[(df['column1'] > 5) & (df['column2'] < 10),"\n"])

