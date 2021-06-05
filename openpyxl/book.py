from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# create a workbook
wb = Workbook()
# create a worksheet reference in current workbook
ws = wb.active
# create new sheets (in 3 ways)
ws1 = wb.create_sheet('NewSheet')
ws2 = wb.create_sheet('Another', 0)
ws.title = 'Mysheet'

print(wb.sheetnames)




# create a new workbook
wb2 = load_workbook('regions.xlsx')
# create a new sheet
new_sheet = wb2.create_sheet('NewSheet')
# create a reference, just like activate copyversion
active_sheet = wb2.active
# read cell value
cell = active_sheet['A1']
print(cell.value)
# change cell value
active_sheet['A1'] = 0
wb2.save('modified.xlsx')


