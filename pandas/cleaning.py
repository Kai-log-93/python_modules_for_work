import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
# specify header for CSV
df.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']

df.drop(columns='Address', inplace=True)

df = df.set_index('Area Code')

# select specific column from indexed location 
print(df.loc[8074:, 'First'])
print('---------------------')

# select fiest row
print(df.iloc[0])
print('---------------------')

# split string by space into column
print(df.First.str.split(expand=True))
print('---------------------')

# select the first column of splited first column
df.First = df.First.str.split(expand=True)
print(df)

# replace the NaN then to excel
df = df.replace(np.nan, 'N/A', regex=True)
to_excel = df.to_excel('modified.xlsx')






