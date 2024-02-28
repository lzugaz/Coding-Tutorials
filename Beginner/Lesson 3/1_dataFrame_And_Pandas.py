# Python and Pandas for Data Analysis

# Part 1: Introduction to Data Reading with Pandas
import pandas as pd  # Importing the pandas library, essential for data manipulation and analysis.

# Reading data is the first step in data analysis. Pandas supports various formats, including Excel and CSV.
# Here's how to read data from an Excel file into a DataFrame, a powerful data structure in pandas.
df = pd.read_excel('LifeExpProjectData.xlsx', header=0)
# 'header=0' indicates that the first line of the file contains column names.

# Part 2: Viewing Data
# Once data is loaded into a DataFrame, it's important to explore its structure and content.
# The head() function displays the first few rows of the DataFrame.
print("First 5 rows of the DataFrame:")
print(df.head())
# Use head(n) to display the first 'n' rows.

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))
# Similarly, tail() shows the last few rows, useful for understanding the end of your dataset.
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# Part 3: Basic Data Exploration
# Before diving into complex data manipulations, start with basic DataFrame operations.
# The describe() function provides a statistical summary of numerical columns, a quick way to understand data distribution.
print("\nStatistical summary of the DataFrame:")
print(df.describe())

# Selecting data is another fundamental operation. Here's how to select a single column.
print("\nSelecting a single column ('Country'):")
print(df['Country'].head())

# Part 4: Intermediate Data Manipulation
# Working with subsets of data can be very useful. For example, filtering data based on conditions.
print("\nCountries with life expectancy greater than 75 years:")
high_life_exp = df[df['2015Life.expectancy'] > 75]
print(high_life_exp[['Country', '2015Life.expectancy']])

# Handling missing data is a common task. You can fill missing values with a specified value or the mean of the column.
print("\nHandling missing data:")
df_filled = df.fillna(value={'Medical doctors': df['Medical doctors'].mean()})
print(df_filled.head())

# Grouping data is powerful for analysis. The groupby() function groups data by a certain criterion.
print("\nAverage life expectancy and medical resources by first letter of country:")
grouped = df.groupby(df['Country'].str[0])[['2015Life.expectancy', 'Medical doctors', 'Nurses', 'Pharmacists']].mean()
print(grouped.head())

# Merging DataFrames is similar to SQL joins and allows for combining datasets based on a common column.
print("\nDataFrame merged with continents:")
df_with_continent = pd.merge(df, pd.DataFrame({
    'Country': ['Afghanistan', 'Albania', 'Algeria', 'Australia', 'Austria'],
    'Continent': ['Asia', 'Europe', 'Africa', 'Oceania', 'Europe']
}), on='Country', how='left')
print(df_with_continent.head())

# Part 5: Data Visualization
# Visualizing data is crucial for understanding and communicating findings. Pandas integrates with Matplotlib for plotting.
# This is just an example of using visualization, but please try and make your own.
print("\nVisualizing life expectancy:")
import matplotlib.pyplot as plt
df_sorted = df.sort_values('2015Life.expectancy', ascending=False)
plt.figure(figsize=(10, 8))
plt.barh(df_sorted['Country'][:10], df_sorted['2015Life.expectancy'][:10])
plt.xlabel('Life Expectancy')
plt.ylabel('Country')
plt.title('Top 10 Countries by Life Expectancy in 2015')
plt.show()

# This tutorial covers the basics of data analysis with pandas, from reading data and exploration, to manipulation, merging, and visualization.
# Experiment with these techniques to gain deeper insights into your datasets.
