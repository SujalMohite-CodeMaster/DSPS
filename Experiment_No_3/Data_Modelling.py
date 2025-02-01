"""Data Modelling
1.Indentify the total number of records in the trainging data set.
2.Validate your partition by performing a  two-sample Z-test.
"""
import pandas as pd
import numpy as  np

# loading the data sets.
file_path = r"C:\Users\mohit\Downloads\Registered Students of TE for Edunet Foundation's Training (157).xlsx"

xls = pd.ExcelFile(file_path)
print(xls.sheet_names)
df = pd.read_excel(file_path, sheet_name="Batch 2")

total_records = df.shape[0]
print(f"Total number of records in the training data set: {total_records}")

