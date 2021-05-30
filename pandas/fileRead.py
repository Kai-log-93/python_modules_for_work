import pandas as pd
from openpyxl.workbook import Workbook

# for understanding Pandas 
# in pandas 
#excel and txt data is formated differently

df_excel = pd.read_excel('regions.xlsx')
# you can spefify if the file has a header in csv file
df_csv = pd.read_csv('Names.csv', header=None)
# specify header for CSV
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code', '']
# you can specify the delimiter in txt data
df_txt = pd.read_csv('data.txt', delimiter='\t')


df_csv.to_excel('modified.xlsx')