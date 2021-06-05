from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = load_workbook('regions.xlsx')
ws = wb.active

# print A1-C1 cell information
cell_range = ws['A1': 'C1']
print(cell_range)
print('---------------------------')

# print column C all cells' information
col_c = ws['C']
print(col_c)
print('---------------------------')

# get A:C column all cells information
col_range = ws['A': 'C']
print(col_range)
print('---------------------------')

# get spcific row cells information
row_range = ws[1:5]
print(row_range)
print('---------------------------')

# get A1 : C2 all cell information
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)



