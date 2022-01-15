import pandas as pd
import os

print(os.getcwd())
print(os.listdir())


"""
Pandas Dataframes
"""
dataset = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passing': [3, 7, 2]
}

# pandas Datafram is a labeled data structure with rows/columns of potentially different types
# think of a Dataframe as something like spreadsheets or SQL table
data_var = pd.DataFrame(dataset)
print(data_var)

# using the loc attribute allows me to locate a row and see the items in that row 
# loc returns a pandas Series
print(data_var.loc[0])

# loc can take in mutilple rows
print(data_var.loc[[0, ]])

# TODO: create a CSV to practice loading files into Dataframes
# Loading files in to a pandas DataFrame
df = pd.read_csv('data.csv')
print(df)
"""
Pandas Series
"""
# pandas Series is like a column in a table 
a = [1, 7, 2]

series_var = pd.Series(a)
print(series_var)


# pandas Labels will label values with their index number if nothing else is speciied
# personal labels can be given to a series with the index argument
label_series = pd.Series(a, index=['x', 'y', 'z'])
print(label_series)
# when creating labels, I can now access an item referring to the created lable like an index
print(label_series['x'])
# also use key:value pairs (like a dict) to label a series during creation 
calories = {'day1': 420, 'day2': 380, 'day3': 390}
daily = pd.Series(calories)
print(daily)
# I can also specify the items I want with index argument 
specific_days = pd.Series(calories, index=['day1', 'day2'])
print(specific_days)