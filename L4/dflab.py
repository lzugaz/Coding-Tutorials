import pandas as pd

# Introduction to reading data
# Explain the importance of reading data from different sources, like Excel, CSV, etc.
# Here, we're reading from an Excel file into a pandas DataFrame.
df = pd.read_excel('LifeExpProjectData.xlsx', header=0)

# Introduction to viewing data
# Explain that viewing the data is a crucial step for understanding its structure and contents.
# The `head()` function shows the first few rows of the DataFrame, providing a quick overview.
print("First 5 rows of the DataFrame:")
print(df.head())

# Mention how you can change the number of rows displayed by passing a parameter to `head()`.
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

# Similarly, introduce the `tail()` function, which shows the last few rows, useful for seeing the end of the dataset.
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# Intermediate exploration
# Before diving into more complex manipulations, encourage exploring the dataset using basic DataFrame operations.
# For example, using `describe()` to get a statistical summary of numerical columns.
print("\nStatistical summary of the DataFrame:")
print(df.describe())

# Introduce the concept of indexing and selecting data
# Show how to select a single column or multiple columns.
print("\nSelecting a single column ('Country'):")
print(df['Country'].head())

# Data manipulation: Splitting DataFrame by the first letter of a country
# Provide the rationale: For large datasets, it might be useful to work with smaller subsets.
# Here, we're creating subsets of the data based on the first letter of the 'Country' column.

# Explain the approach: using a for loop and string operations to categorize countries.
dfs = {}
for letter in df['Country'].str[0].unique():
    # This line filters the DataFrame for countries starting with the current letter in the loop.
    dfs[letter] = df[df['Country'].str.startswith(letter)]

# Demonstrating the result
# Access and display the DataFrame for countries starting with a specific letter, such as 'B'.
print("\nDataFrame for countries starting with 'B':")
if 'B' in dfs:
    print(dfs['H'])
else:
    print("No countries starting with 'B'.")

# Encourage exploration
# Suggest students to try accessing DataFrames for different letters and explore the data further.
# For example, analyzing life expectancy or healthcare resources by regions or alphabetical groups.
    
# Advanced Data Manipulation

# Filtering Data
# Teach how to filter rows based on conditions. For example, selecting countries with life expectancy greater than a certain value.
print("\nCountries with life expectancy greater than 75 years:")
high_life_exp = df[df['2015Life.expectancy'] > 75]
print(high_life_exp[['Country', '2015Life.expectancy']])

# Working with Missing Data
# Introduce how to handle missing data, a common task in data analysis.
# For instance, you can show how to drop rows with any missing values or fill them with a default value.
print("\nHandling missing data:")
df_filled = df.fillna(value={'Medical doctors': df['Medical doctors'].mean()})
print(df_filled.head())

# Grouping and Aggregating Data
# Explain how to use `groupby()` for grouping data and performing aggregate functions.
# This could involve grouping by a categorical variable and calculating averages for numerical columns.
print("\nAverage life expectancy and medical resources by first letter of country:")
grouped = df.groupby(df['Country'].str[0])[['2015Life.expectancy', 'Medical doctors', 'Nurses', 'Pharmacists']].mean()
print(grouped.head())

# Merging DataFrames
# Introduce the concept of merging/joining DataFrames, similar to SQL joins.
# You might need to create or imagine a second DataFrame to demonstrate this.
# For example, a DataFrame mapping countries to continents could be merged with the current DataFrame.
continents = pd.DataFrame({
    'Country': ['Afghanistan', 'Albania', 'Algeria', 'Australia', 'Austria'],
    'Continent': ['Asia', 'Europe', 'Africa', 'Oceania', 'Europe']
})
df_with_continent = pd.merge(df, continents, on='Country', how='left')
print("\nDataFrame merged with continents:")
print(df_with_continent.head())

# Visualization
# Introduce basic data visualization using pandas plotting capabilities or matplotlib.
# For example, plotting the life expectancy of countries.
print("\nVisualizing life expectancy:")
import matplotlib.pyplot as plt

# Ensure the DataFrame is sorted by life expectancy for more meaningful visualization.
df_sorted = df.sort_values('2015Life.expectancy',ascending = False)
plt.figure(figsize=(10, 8))
plt.barh(df_sorted['Country'][:10], df_sorted['2015Life.expectancy'][:10])  # Top 10 countries by life expectancy
plt.xlabel('Life Expectancy')
plt.ylabel('Country')
plt.title('Top 10 Countries by Life Expectancy in 2015')
plt.show()





