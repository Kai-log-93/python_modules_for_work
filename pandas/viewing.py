import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('Names.csv', header=None)
# specify header for CSV
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', '']

# only print column 'Last'
print(df_csv['Last'])
print('----------------------------------')
# print 2 columns
print(df_csv[['State', 'Area Code']])
print('----------------------------------')
# print  first 3 row
print(df_csv['First'][0:3:1])
print('----------------------------------')
# locate  record
print(df_csv.iloc[2,1])

# only get wanted value to excel
wanted_value = df_csv[['First','Last','State']]
stored = wanted_value.to_excel('State_Location.xlsx')
