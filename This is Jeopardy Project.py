import pandas as pd
pd.set_option('display.max_colwidth', None)
# Load the Jeopardy dataset

jeopardy = pd.read_csv("jeopardy.csv")

print(jeopardy.head())
print(jeopardy.columns)

# Change names of columns to remove spaces from the beginning
jeopardy.columns = [col.strip() for col in jeopardy.columns]
# Display the dataset information
print(jeopardy.describe(include='all'))  # Provides a summary of the dataset
# Display the first 10 rows of the dataset
print(jeopardy.head(10))  # Shows the first 10 rows
print(jeopardy.columns)  # Displays the column names

# Function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame of 152 rows. Every row had the strings "King" and "England" somewhere in its " Question".
def filter_by_words(df, words):
    contains_all = df['Question'].apply(lambda x: all(word.lower() in x.lower() for word in words))
    return df[contains_all] 
# Example usage of the filter function
filtered_df = filter_by_words(jeopardy, ["King", "England"])
print(filtered_df.head())  # Display the first few rows of the filtered DataFrame

