#!/data/tsel/bi20/wipro/anaconda3/bin/python

import pandas as pd
import sys
import re

# First Argument is treated as delimiter of actual file, Valid Values Are { ; or | or \t etc)
# Second Argument is a Flag to check whther to Merge or Ignore extra columns, Valid Values Are { Y or N}
# Third Argument is the Total Number of Expected Records, Valid values are any numeric value
# Third Argument is What's the Seperater to use to merge columns

sys.stdin.reconfigure(encoding="ISO-8859-1")
#sys.stdin.reconfigure(encoding="UTF-8")

input_seperator = sys.argv[1]

df = pd.read_csv(sys.stdin,engine="python", sep=sys.argv[1], index_col = False, header=None, dtype="str")

#print(df)

start_len = int(sys.argv[3])-1
total_len = len(df.columns)-1

try:
    if (sys.argv[2] == "Y"):
        df[df.columns[total_len]] = df[df.columns[start_len:]].apply(lambda x: sys.argv[4].join(x.dropna().astype(str)),axis=1)
        df.drop(df.iloc[:, start_len:total_len], inplace = True, axis = 1)
        df.to_csv(sys.stdout, index=False, sep=input_seperator, header=False)
    else:
        df.iloc[:, 0: start_len+1].to_csv(sys.stdout, index=False , sep=input_seperator)
except:
    print("Error in execution, Please check the arguments are passed in proper order")



