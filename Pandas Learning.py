# Pandas Learning – Codecademy Course
# Author: Jose Peon
# Path: AI Engineer Path → Pandas Learning

import pandas as pd

# --- Basic Pandas Objects ---

# Series
print("\n--- Pandas Series ---")
s = pd.Series([1, 2, 3])
print(s)

# DataFrame
print("\n--- Pandas DataFrame ---")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})
print(df)

# Indexing and Slicing
print("\n--- Indexing and Slicing ---")
print("First row of DataFrame:")
print(df.iloc[0])  # Using iloc for positional indexing
print("First two rows of DataFrame:")
print(df.iloc[:2])  # Slicing the first two rows        

# Accessing columns
print("\n--- Accessing Columns ---")
print("Accessing 'Name' column:")
print(df["Name"])  # Accessing a single column
print("Accessing multiple columns:")
print(df[["Name", "Age"]])  # Accessing multiple columns

# Adding a new column
print("\n--- Adding a New Column ---")
df["City"] = ["New York", "Los Angeles", "Chicago"]
print("DataFrame after adding 'City' column:")
print(df)

# Renaming columns
print("\n--- Renaming Columns ---")
df.rename(columns={"Name": "Full Name", "Age": "Years"}, inplace=True)
print("DataFrame after renaming columns:")
print(df)

# Deleting a column
print("\n--- Deleting a Column ---")
df.drop(columns=["City"], inplace=True)
print("DataFrame after deleting 'City' column:")
print(df)

# Filtering DataFrame
print("\n--- Filtering DataFrame ---")
filtered_df = df[df["Years"] > 28]
print("Filtered DataFrame (Years > 28):")
print(filtered_df)

# Sorting DataFrame
print("\n--- Sorting DataFrame ---")
sorted_df = df.sort_values(by="Years", ascending=False)
print("DataFrame sorted by 'Years' in descending order:")
print(sorted_df)    

# Grouping DataFrame
print("\n--- Grouping DataFrame ---")
grouped_df = df.groupby("Full Name").mean()  # Example of grouping, though not much data to group
print("Grouped DataFrame (mean):")
print(grouped_df)

# Handling missing data
print("\n--- Handling Missing Data ---")
df_with_nan = df.copy()
df_with_nan.loc[1, "Years"] = None  # Introduce a NaN
print("DataFrame with NaN:")
print(df_with_nan)
print("DataFrame after filling NaN with 0:")
print(df_with_nan.fillna(0))  # Filling NaN with 0  

# Merging DataFrames
print("\n--- Merging DataFrames ---")
df2 = pd.DataFrame({
    "Full Name": ["Alice", "Bob", "David"],
    "Salary": [70000, 80000, 60000]
})
merged_df = pd.merge(df, df2, on="Full Name", how="outer")
print("Merged DataFrame:")
print(merged_df)

