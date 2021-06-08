import pandas as pd

df_1 = pd.read_excel('shifts.xlsx', sheet_name='Sheet')
df_2 = pd.read_excel('shifts.xlsx', sheet_name='Sheet1')
df_3 = pd.read_excel('shift_3.xlsx')

df_all = pd.concat([df_1,df_2,df_3], sort=False)
print(df_all.groupby(['Shift']).mean()['Units Sold'])




to_excel = df_all.to_excel('all_shifts.xlsx', index=None)






