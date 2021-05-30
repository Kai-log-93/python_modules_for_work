import pandas as pd
from openpyxl.workbook import Workbook



df_csv = pd.read_csv('Names.csv', header=None)
# specify header for CSV
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', 'Income']


# get City == 'Riverside'
print(df_csv.loc[df_csv['City'] == 'Riverside'])
print('-------------------------------------------')
# get City == 'Riverside' and First == 'John'
print(df_csv.loc[(df_csv['City'] == 'Riverside') & (df_csv['First'] == 'John')])
print('-------------------------------------------')
# Lamda funtion base on income get the tax rate
df_csv['Tax %'] = df_csv['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)
print(df_csv)
print('-------------------------------------------')
# get Taxes
df_csv['Texes Owed'] = df_csv['Income'] * df_csv['Tax %'] 
print(df_csv['Texes Owed'])
print(df_csv)
print('-------------------------------------------')
# drop collums
to_drop = ['Area Code', 'First', 'Address']
df_csv.drop(columns = to_drop, inplace = True)
print(df_csv)
print('-------------------------------------------')
# boolean
df_csv['Test col'] = False
df_csv.loc[df_csv['Income'] < 60000, 'Test Col'] = True
print(df_csv)
print('-------------------------------------------')
# group by
print(df_csv.groupby(['Test Col']).mean().sort_values('Income'))
