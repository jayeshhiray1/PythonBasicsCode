# importing pandas as pd
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Weight': [45, 88, 56, 15, 71],
                   'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
                   'Age': [14, 25, 55, 8, 21]})

# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']

# Set the index
df.index = index_

# Print the DataFrame
print(df)

# return the column labels DataFrame
result = df.columns

# Print the result
print("Result is "+result)
total_len = len(df.columns)-1
print(df.columns[total_len])
#print one columns DataFrame
print(df[df.columns[total_len]])
#print how many rows in table/DataFrame
print(len(df[df.columns[total_len]]))

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

