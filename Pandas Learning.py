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
dfe = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})
print(dfe)

# Indexing and Slicing
print("\n--- Indexing and Slicing ---")
print("First row of DataFrame:")
print(dfe.iloc[0])  # Using iloc for positional indexing
print("First two rows of DataFrame:")
print(dfe.iloc[:2])  # Slicing the first two rows        

# Accessing columns
print("\n--- Accessing Columns ---")
print("Accessing 'Name' column:")
print(dfe["Name"])  # Accessing a single column
print("Accessing multiple columns:")
print(dfe[["Name", "Age"]])  # Accessing multiple columns

# Adding a new column
print("\n--- Adding a New Column ---")
dfe["City"] = ["New York", "Los Angeles", "Chicago"]
print("DataFrame after adding 'City' column:")
print(dfe)

# Renaming columns
print("\n--- Renaming Columns ---")
dfe.rename(columns={"Name": "Full Name", "Age": "Years"}, inplace=True)
print("DataFrame after renaming columns:")
print(dfe)

# Deleting a column
print("\n--- Deleting a Column ---")
dfe.drop(columns=["City"], inplace=True)
print("DataFrame after deleting 'City' column:")
print(dfe)

# Filtering DataFrame
print("\n--- Filtering DataFrame ---")
filtered_dfe = dfe[dfe["Years"] > 28]
print("Filtered DataFrame (Years > 28):")
print(filtered_dfe)

# Sorting DataFrame
print("\n--- Sorting DataFrame ---")
sorted_dfe = dfe.sort_values(by="Years", ascending=False)
print("DataFrame sorted by 'Years' in descending order:")
print(sorted_dfe)    

# Grouping DataFrame
print("\n--- Grouping DataFrame ---")
grouped_dfe = dfe.groupby("Full Name").mean()  # Example of grouping, though not much data to group
print("Grouped DataFrame (mean):")
print(grouped_dfe)

# Handling missing data
print("\n--- Handling Missing Data ---")
dfe_with_nan = dfe.copy()
dfe_with_nan.loc[1, "Years"] = None  # Introduce a NaN
print("DataFrame with NaN:")
print(dfe_with_nan)
print("DataFrame after filling NaN with 0:")
print(dfe_with_nan.fillna(0))  # Filling NaN with 0  

# Merging DataFrames
print("\n--- Merging DataFrames ---")
dfe2 = pd.DataFrame({
    "Full Name": ["Alice", "Bob", "David"],
    "Salary": [70000, 80000, 60000]
})
merged_dfe = pd.merge(dfe, dfe2, on="Full Name", how="outer")
print("Merged DataFrame:")
print(merged_dfe)

#Codecademy Course Exercises
print("\n--- Codecademy Course Exercises ---")
print("\n--- Adding Column I ---\n")

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

print(df)

print("\n--- Adding Column II ---\n")
# Add a new column to the DataFrame

df['Is taxed?'] = "Yes"
print(df)

print("\n--- Adding Column III ---\n")
# Add a new column to the DataFrame
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)

print("\n--- Performing Column Operations ---\n")
# Perform operations on columns
df["Lowercase Name"] = df.Name.apply(str.lower)
print(df)

print("\n--- Reviewing Lambda Function ---\n")
mylambda = lambda string: string[0] + string[-1] if len(string) >= 2 else "Not longer than two characters"
print("Lambda function example:")
print(mylambda("Hello"))
print(mylambda("A"))

print("\n--- Reviewing Lambda Function: If Statements ---\n")
mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else "You must be 13 or older"
print("Lambda function with if statement:")
print(mylambda(15))
print(mylambda(10))


