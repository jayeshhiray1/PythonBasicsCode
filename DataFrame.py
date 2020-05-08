# import pandas as pd
import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.
#---------------------------------------------
print("===Python code demonstrate creating DataFrame from dict narray===")
# intialise data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)

print("=== Column Selection: In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name==")

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])

print("==============Splitting and Replacing a Data==================")
# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# dropping null value columns to avoid errors
df.dropna(inplace=True)

# new data frame with split value columns
df["Address"] = df["Address"].str.split("a", n=1, expand=True)

# df display
print(df)