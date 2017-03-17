"""This is a script to parse child labor and child marriage data.
The excel file used in this script can be found here.
https://www.unicef.org/sowc2014/numbers/
"""

import xlrd
import pprint
book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet = book.sheet_by_name('Table 9 ')                      # need to consider whitespace in tabs name

count = 0                                                   # put counter to 0
data = {}                                                   # create an empty dictionary

# loop over rows starting in row 14 where the data set start up until last row of excel file
for i in xrange (14, sheet.nrows):
    row = sheet.row_values(i)                               # assign row value i to row object
    country = row[1]                                        # second column of row equals country name assign to object

    data[country] = {                                       # create key in data dict with value of country object and another dictionary as value
        'child_labor':{
            'total': [row[4],row[5]],                       # fill in data from excel file column 5 & 6 etc.
            'male':[row[6],row[7]],
            'female':[row[8],row[9]],
        },
        'child_marriage':{
            'married_by_15':[row[10],row[11]],
            'married_by_18':[row[12],row[13]],
        }
    }
    if country == 'Zimbabwe':                               # break if you reach Zimbabwe
        break

print data['Afghanistan']
pprint.pprint(data)

### try to use pandas --> pandas more to use organized data

import pandas as pd
import os

base_dir = r'C:\Users\dallmi\PycharmProjects\DataWrangling'
fname = 'SOWC 2014 Stat Tables_Table 9.xlsx'
in_path = os.path.join(base_dir,fname)

df = pd.read_excel(in_path)



