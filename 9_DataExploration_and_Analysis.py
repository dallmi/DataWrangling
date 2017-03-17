# read excel file in
import xlrd

workbook = xlrd.open_workbook('unicef_oct_2014.xls')
workbook.nsheets
workbook.sheet_names()

sheet = workbook.sheets()[0]            # selecting the sheet for import into agate library
sheet.nrows                             # identifies how many rows in our sheet
sheet.row_values(0)                     # selects a single row within excel and shows values

# look at data
for r in range(sheet.nrows):
    print r, sheet.row(r)               # By using range and for loop we can see how python sees the data. row method returns information on data and data type of each row

title_rows = zip(sheet.row_values(4), sheet.row_values(5))      # get headers from row 4 and 5

# create headers - agate library expects a tuple list where first value is the title string
titles = [t[0] +' ' + t[1] for t in title_rows]                 # bring tuple into one list with strings, but creates leading spaces
titles = [t.strip() for t in titles]                            # remove leading and trailing spaces

# rows with data we want to use are between 6-114
country_rows = [sheet.row_values(r) for r in range (6, 114)]


# ============================================================================================== agate data types

from xlrd.sheet import ctype_text
import agate

text_type = agate.Text()
number_type = agate.Number()
boolean_type = agate.Boolean()
date_type = agate.Date()

example_row = sheet.row(6)      # populate an example row with data, which then can be used to determine data types for each column

print example_row               # visual check of the data to see if xlrd identifies all data

print example_row[0].ctype      # get type and value of cell
print example_row[0].value

print ctype_text                # returns data type as text i.e. ctype_text[3] returns 'xldate'

# loop through example row and use ctype to match column types
types = []
for v in example_row:
    value_type = ctype_text[v.ctype]        # converts/maps ctype number into ctype_text to make data type readable
    if value_type == 'text':                # match value_type with agate column types into a list
        types.append(text_type)
    elif value_type == 'number':
        types.append(number_type)
    elif value_type == 'xldate':
        types.append(date_type)
    else:                                   # if there is no type use text column type
        types.append(text_type)

table = agate.Table(country_rows, titles, types)    # will throw an error due to bad data records

# cleaning bad data
def remove_bad_chars(val):                  # remove characters like '-'
    if val == '-':
        return None                         # returns None if val = '-'
    return val

# cleanse the data in a first step very specific and then you can write a helper function in next step
cleaned_rows = []
for row in country_rows:
    cleaned_row = [remove_bad_chars(rv) for rv in row]  #iterates through row to create cleaned rows
    cleaned_rows.append(cleaned_row)                    # creates a cleaned_rows list holding clean data

# write a helper function to clean data, makes above 3 lines generic
def get_new_array(old_array, function_to_clean):            # two input arguments old data array and function to clean the data
    new_arr = []
    for row in old_array:
        cleaned_row = [function_to_clean(rv) for rv in row]
        new_arr.append(cleaned_row)
    return new_arr                                          # returns cleaned array as a list

cleaned_rows = get_new_array(country_rows, remove_bad_chars) # calls function with remove_bad_char function and saves it in cleaned_rows


table = agate.Table(cleaned_rows, titles, types)
table.print_table(max_columns=7)                    # not sure why I get an error here????? --> had to change agate python script preview for it to work --> https://github.com/datadesk/agate/blob/c9e0b0ecbec4140f8c1df4eaf1b9307b7c4fb42b/agate/preview.py
table.print_structure()

# =========== Exploring Table Functions (sort, filter, compute, rank)==================================
table.column_names

most_eregious = table.order_by('Total (%)', reverse=True).limit(10)
most_eregious.print_table()

for r in most_eregious.rows:
    print r

most_females = table.order_by('Female', reverse=True).limit(10)
for r in most_females.rows:
    print '{}: {}%'.format(r['Countries and areas'], r['Female'])       # you get some None values back

female_data = table.where(lambda r: r['Female'] is not None)            # ensure each row has a value for 'Female' column
female_data.print_table()

most_females = female_data.order_by('Female',reverse=True).limit(10)
most_females.print_table()

for r in most_females.rows:
    print '{}: {}%'.format(r['Countries and areas'], r['Female'])

# what's the average percentage of child labor in cities
table.aggregate(agate.Mean('Place of residence (%) Urban'))                         # results in error due to None values
has_por = table.where(lambda r: r['Place of residence (%) Urban'] is not None)
has_por.print_table()

has_por.aggregate(agate.Mean('Place of residence (%) Urban'))

# rows with more than 50% rural child labor
first_match = has_por.find(lambda r: r['Place of residence (%) Urban'] > 50)
first_match['Countries and areas']                          # not sure why get NoneType object has no attribute '__getitem__'

ranked = table.compute([('Total Child Labor Rank',agate.Rank('Total (%)', reverse=True)), ])    # insert Rank column based Total column descending = reverse
ranked.order_by('Total (%)', reverse=True).print_table()                                        # sort table descending by Total column

for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print row['Countries and areas'], row['Total (%)'], row ['Total Child Labor Rank']

# returns inverse percentage if given a row
def reverse_percent(row):
    return 100-row['Total (%)']

ranked = table.compute([('Children not working (%)', agate.Formula(number_type, reverse_percent)), ])
ranked = ranked.compute([('Total Child Labor Rank', agate.Rank('Children not working (%)')), ])

ranked.print_table()

for row in ranked.order_by('Total (%)', reverse=True).limit(20).rows:
    print row['Total (%)'], row ['Total Child Labor Rank']

# ========= JOINING NUMEROUS DATASETS ================================