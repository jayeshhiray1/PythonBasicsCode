# import pandas as pd
import pandas as pd

# import numpy as np
import numpy as np

# simple array
data = np.array(['g','e','e','k','s'])

ser = pd.Series(data)
print(ser)

# a simple list
list = ['g', 'e', 'e', 'k', 's']

print("create series form a list")

ser=pd.Series(list)
print(ser)

# creating simple array
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)

print("Retrieve the first 5 element")
print(ser[:5])