from openpyxl.styles import Font,colors,Alignment,PatternFill, GradientFill, Border, Side
from openpyxl.styles import NamedStyle
from openpyxl.workbook import Workbook

wb = Workbook()
ws = wb.active


for i in range(1,20):
    ws.append(range(300))

# merge cells
ws.merge_cells('A1:B5')
ws.unmerge_cells('A1:B5')
ws.merge_cells(start_row=2, start_column=2, end_row=5, end_column=5)

# set cell font style
cell = ws['B2']
cell.font = Font(color='FF000000', size=20, italic=True)
# set cell value
cell.value = 'Merged Cell'
# set cell alignment
cell.alignment = Alignment(horizontal='right', vertical='bottom')
# GradientFill
cell.fill = GradientFill(stop=('000000', 'FFFFFF'))
wb.save('text.xlsx')



























