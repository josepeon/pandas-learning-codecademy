import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('diabetes.csv')

# Display the first few rows of the dataset
print(data.head(10))
# Display basic statistics of the dataset
print(data.describe())

# Display the data types of each column
print(data.dtypes)
print(data.columns)
# Check for missing values

data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

print(data.info())
print(data.isnull().sum())
print(data[data.isnull().any(axis=1)])

print(data.Outcome.unique())

#Replace instances of 'O' with 0 and convert the Outcome column to type int64.

data['Outcome'] = data['Outcome'].replace('O', 0).astype('int64')   
# Display the unique values in the Outcome column
print(data['Outcome'].unique())
