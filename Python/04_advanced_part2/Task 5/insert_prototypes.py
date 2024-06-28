import openpyxl
import re

header_file = 'prototypes.h'
excel_file = 'excel.xlsx'

with open(header_file, 'r') as f:
    copy = f.read()

prototypes_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([a-zA-Z0-9_\s,]*\)\s*;$'
prototypes = re.findall(prototypes_pattern, copy)

workbook = openpyxl.Workbook()
sheet = workbook.active 

row = 1
ID_counter = 1
for p in prototypes:
    sheet.cell(row=row, column=1, value=p)
    sheet.cell(row=row, column=2, value=f'IDX{ID_counter}')
    row+=1
    ID_counter+=1

workbook.save(excel_file)

