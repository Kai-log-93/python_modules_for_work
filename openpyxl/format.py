from openpyxl import styles
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
cell.font = Font(color='FF0000', size=20, italic=True)
# set cell value
cell.value = 'Merged Cell'
# set cell alignment
cell.alignment = Alignment(horizontal='right', vertical='bottom')
# GradientFill
cell.fill = GradientFill(stop=('000000', 'FFFFFF'))
wb.save('text.xlsx')

highlight = NamedStyle(name='hightlight')
highlight.font = Font(bold=True)
bd = Side(style='thick', color='000000')
highlight.border = Border(left=bd,top=bd,right=bd,bottom=bd)
highlight.fill = PatternFill('solid',fgColor='FFFF00')

count = 0
for col in ws.iter_cols(min_col=8, min_row=1, max_col=30, max_row=30):
    col[count].style = highlight
    count += 1

wb.save('hightlight.xlsx')





























