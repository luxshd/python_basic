import openpyxl
rows_cnt = 51
file_name = 'data.xlsx'
book = openpyxl.open(file_name, read_only=True)
sheet = book.active
row = 1
print(sheet[row][0])

