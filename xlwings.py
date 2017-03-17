import xlwings as xw
import pandas as pd

app = xw.App()
app.books['Book1']

wb = xw.Workbook()      # this will create a new workbook
xw.Workbook(r'C:\Users\dallmi\PycharmProjects\DataWrangling\xlwings_test.xlsx')


sht = wb.Sheets['Sheet1']   # why are you not working anymore?



xw.Range('A1').value = 'something'
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
xw.Range('A1').value = df                                   # copies df into excel
xw.Range('A1').options(pd.DataFrame, expand='table').value