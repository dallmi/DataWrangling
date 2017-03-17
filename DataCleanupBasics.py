from csv import DictReader

# use Dict reader
data_rdr = DictReader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn.csv', 'rb'))
header_rdr = DictReader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn_headers.csv','rb'))


# creates a list of dictionaries. For each row one dictionary with key = column headers and value = entries of that row
data_rows = [d for d in data_rdr]                   # creates one dictionary for each row with key = header name short and value = data content
header_rows = [h for h in header_rdr]               # creates one dictionary for each row with key = header and value = data content --> data content contains short names and long names, sort of mapping table

print data_rows [:5]
print header_rows [:5]

new_rows = []

for data_dict in data_rows:                                     # 1st loop through all dicts in list of dicts mn.csv file (one list of dict represents one row of excel data, whereas the key always represents the header and value the data content of the key)
    new_row = {}                                                # create a new dictionary for each existing dictionary (because the new one will contain the long column headers rather than the abbreviations)
    for dkey, dval in data_dict.items():                        # loop through key(column header), value(cell content) pairs of data_dict from data_rows (contains the raw data)
        for header_dict in header_rows:                         # 2nd loop to go through all dictionaries within the mn_headers.csv file
            if dkey in header_dict.values():                    # if short name exists in values of header_dict then do ...
                new_row[header_dict.get('Label')] = dval        # create entry in new dict with long name as key (header) and dval as row values
    new_rows.append(new_row)                                    # create one list for each data_dict

new_rows[0]

#==============================================================================================================================================================================================================================================================================
# Use simple reader instead of Dict reader to elaborate the Zip functionality
from csv import reader

data_rdr = reader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn.csv', 'rb'))
header_rdr = reader (open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn_headers.csv','rb'))

data_rows = [d for d in data_rdr]           # creaes list of lists, first list = column headers, second list = row 1, third list row2, etc.
header_rows = [h for h in header_rdr]       # creaes list of lists, first list = column headers, second list = row 1, third list row2, etc.

print len(data_rows[0])                     # first row of data represents all short name headers
print len(header_rows)                      # list of short header names in first column, hence transformed format of data rows

bad_rows = []

for h in header_rows:                       # for each cell in header_rows
    if h[0] not in data_rows[0]:            # check if short name header is missing in data set;     h[0] = first entry of each header_rows list = short name column header;        data_rows[0] = header row of data set
        bad_rows.append(h)                  # append missing short name header to bad rows list

for h in bad_rows:
    header_rows.remove(h)                   # remove header rows which do not exist in data_rows header

print len(header_rows)

all_short_headers = [h[0] for h in header_rows] # create a list with first entry of each list (column 1)

for header in data_rows[0]:
    if header not in all_short_headers:
        print 'mismatch!',header

# ==============================================================================================
# With Updated header file
from csv import reader

data_rdr = reader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn.csv', 'rb'))
header_rdr = reader (open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn_headers_updated.csv','rb'))

data_rows = [d for d in data_rdr]           # creaes list of lists, first list = column headers, second list = row 1, third list row2, etc.
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]       # creates list of lists if short header exists in data_rows header, first list = column headers, second list = row 1, third list row2, etc.

print len(header_rows)

all_short_headers = [h[0] for h in header_rows] # create a list with first entry of each list (column 1)

skip_index = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)              # returns indexes to skip, because headers not in short list
        skip_index.append(index)

new_data = []

for row in data_rows[1:]:                               # slices list to hold only survey data, no headers
    new_row = []
    for i,d in enumerate (row):                         # enumerate returns index and value of iterable object
        if i not in skip_index:                         # checks that index not in skip index
            new_row.append(d)                           # creates new list without columns to skip
    new_data.append(new_row)                            # creates new list of lists. After going through each item (column) in data_row, adds new entry to new_data list.

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(header_rows,drow))           # zips each row (now exactly matched with header and data) and adds it to a new arraay, zipped_data.

zipped_data[0]

# ============================================== brings header and data into same order, since zip expects same order
from csv import reader

data_rdr = reader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn.csv', 'rb'))
header_rdr = reader (open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn_headers_updated.csv','rb'))

data_rows = [d for d in data_rdr]           # creaes list of lists, first list = column headers, second list = row 1, third list row2, etc.
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]       # creates list of lists if short header exists in data_rows header, first list = column headers, second list = row 1, third list row2, etc.

print len(header_rows)

all_short_headers = [h[0] for h in header_rows] # create a list with first entry of each list (column 1)

skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i,d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []

for drow in new_data:
    zipped_data.append(zip(final_header_rows, drow))


# ================= FORMATTING DATA ==================================================================

for x in zipped_data[0]:
    print 'Question: {[1]}\nAnswer: {}'.format(x[0],x[1])

example_dict = {
    'float_number': 1324.321325496,
    'very_large_integer': 432154879,
    'percentage': .324,
}

string_to_print = "float: {float_number:.4f}\n"
string_to_print += "integer: {very_large_integer:,}\n"
string_to_print += "percentage: {percentage:.2%}"

print string_to_print.format(**example_dict)

# ===================== FINDING OUTLIERS AND BAD DATA ================================================
# zipped_data is a list of tuples, each tuple representing one row. first element of tuple is a list with the short column name, full question and mostly empty string. Second element of tuple = ANSWER

for answer in zipped_data[0]:       # loop through first row of data (questions, answers)
    if not answer[1]:               # if second entry of tuple (which is the answer does not exist then print)
        print answer

for row in zipped_data:             # loop through all rows of data
    for answer in row:              # loop through all (questions, answers within that row)
        if answer[1] is None:       # if answer is None then print
            print answer

na_count = {}                                       # create a dictionary with questions as keys and count of NA as values
for row in zipped_data:
    for resp in row:
        question = resp[0][1]
        answer = resp [1]
        if answer == 'NA':
            if question in na_count.keys():
                na_count[question] += 1
            else:
                na_count[question] = 1

print na_count

# create dictionary and various datatpyes and count
datatypes = {}

start_dict = {'digit':0, 'boolean':0, 'empty':0, 'time_related':0, 'text':0, 'unknown':0}

for row in zipped_data:                                                 # for each tuple within data set one tuple = 1 row
    for resp in row:                                                    # for each entry within tuple
        question = resp[0][1]                                           # slice --> first entry of tuple is a list with column names --> take second entry of that list (long name of question)
        answer = resp [1]                                               # slice --> second entry of tuple i asnswer
        key = 'unknown'                                                 # default key to unknown
        if answer.isdigit():                                            # if answer is digit then key = digit
            key = 'digit'
        elif answer in ['Yes','No','True','False']:                    # else if answer is yes/no type then key = boolean
            key = 'boolean'
        elif answer.isspace():                                          # else if answer empty consists purely out of spaces then key = empty
            key = 'empty'
        elif answer.find('/') > 0 or answer.find(':') >0:               # else if answer contains typical time stamp signs then key = time_related
            key = 'time_related'
        elif answer.isalpha():                                          # else if answer contains only alphabetic characters then key = text
            key = 'text'
        if question not in datatypes.keys():                            # checks if question already in dictionary.
            datatypes[question] = start_dict.copy()                     # if question not in dict, then add with question as key and start_dict as value (dictionary of dictionary)
        datatypes[question][key] += 1                                   # if question already exists in dict datatypes, then add 1 to question, key dictionary combination

print datatypes

# ========================================================= FINDING DUPES

list_with_dupes = [1,5,6,2,5,6,8,3,8,3,3,7,9]
set_without_dupes = set(list_with_dupes)
print set_without_dupes

first_set = set([1,5,6,2,6,3,6,7,3,7,9,10,321,54,654,432])
second_set = set([4,6,7,432,6,7,4,9,0])

print first_set.intersection((second_set))
print first_set.union(second_set)
print first_set.difference(second_set)
print second_set - first_set
print 6 in second_set
print 0 in first_set

import numpy as np
list_with_dupes = [1,5,6,2,5,6,8,3,8,3,3,7,9]

print np.unique(list_with_dupes, return_index=True)     # index returns first position of values

array_with_dupes = np.array([[1,5,7,3,9,11,23],[2,4,6,8,2,8,4]])
print np.unique(array_with_dupes)

# using list comprehension to create a unique set of keys

for x in enumerate (zipped_data[0]):
    print x

set_of_lines = set ([x[2][1] for x in zipped_data])         # Take 3rd tuple and second entry of tuple. Line number is 3rd column and value is second entry of tuple
uniques = [x for x in zipped_data if not set_of_lines.remove(x[2][1])]
print set_of_lines          # error means output is not unique

set_of_keys = set(['%s-%s-%s' % (x[0][1], x[1][1], x[2][1]) for x in zipped_data])
uniques = [x for x in zipped_data if not set_of_keys.remove('%s-%s-%s' % (x[0][1], x[1][1], x[2][1]))]
print len(set_of_keys)

# =========================================== =========================Fuzzy Matching
from fuzzywuzzy import fuzz

my_records = [{'favorite_book': 'Grapes of Wrath',
                'favorite_movie': 'Free Willie',
                'favorite_show': 'Two Broke Girls',
                },
              {
               'favorite_book': 'The Grapes of Wrath',
                  'favorite_movie':'Free Willy',
                  'favorite_show': '2 Broke Girls',
              }
              ]

print fuzz.ratio(my_records[0].get('favorite_book'),
                 my_records[1].get('favorite_book'))

print fuzz.ratio(my_records[0].get('favorite_movie'),
                 my_records[1].get('favorite_movie'))

print fuzz.ratio(my_records[0].get('favorite_show'),
                 my_records[1].get('favorite_show'))

print fuzz.partial_ratio(my_records[0].get('favorite_book'),
                         my_records[1].get('favorite_book'))

print fuzz.partial_ratio(my_records[0].get('favorite_movie'),
                         my_records[1].get('favorite_movie'))

print fuzz.partial_ratio(my_records[0].get('favorite_show'),
                         my_records[1].get('favorite_show'))


from fuzzywuzzy import process

choices = ['Yes', 'No', 'Maybe', 'N/A']

process.extract('ya', choices, limit=2)
process.extractOne('ya', choices)
process.extract('nope', choices, limit=2)
process.extractOne('nope', choices)

# ================================================================================================== RegEx Matching

# \w            Any alphanumeric character, including underscores
# \d            Any digit
# \s            Any whitespace character
# +             One or more (greedy) of the pattern or character
# \.            The . character
# *             Zero or more (greedy) of the character or pattern (think of this almost as an if)
# |             Either the first pattern, of the next, or the next (like OR)
# [] or ()      Character classes (defining what you expect to see in one character                     A matches [A-C] or (A|B|C)
#               space) and character groupings (defining what you expect to see in a group)
# -             Binds character groups

import re

word = '\w+'                        # alphanumeric characters, but not spaces. plus makes it greedy
sentence = 'Here is my sentence.'

re.findall(word, sentence)          # locates all the pattern matches in a string. Period is missing, since no punctuation is included

search_result = re.search(word, sentence)   # if match is found a match object is returned

search_result.group()                       # the match object's group method returns the matched string

match_result = re.match(word,sentence)      # The match method searches only from the beginning of the string. This operates differently from search

match_result.group()

number = '\d+'
capizalized_word = '[A-Z]\w+'
sentence = 'I have 2 pets: Bear and Bunny.'
search_number = re.search(number, sentence)
search_number.group()

match_number = re.match(number, sentence)
match_number.group()

search_capital = re.search(capizalized_word, sentence)
search_capital.group()

match_capital = re.match(capizalized_word, sentence)
match_capital.group()

name_regex = '([A-Z]\w+) ([A-Z]\w+)'                    # Parantheses are used to define groups
names = 'Barack Obama, Ronald Reagan, Nancy Drew'
name_match = re.match(name_regex, names)                # Here we use the rexex pattern with more than 1 regex group
name_match.group()
name_match.groups()                                     # shows all matches found

name_regex = '(?P<first_name>[A-Z]\w+]) (?P<last_name>[A-Z]\w+])'     # providing a name to each group

for name in re.finditer(name_regex, names):
    print 'Meet {}!'.format(name.group('first_name'))

# ============================================= What to do with Dupe records


from csv import DictReader

# use Dict reader
mn_data_rdr = DictReader(open('C:\Users\dallmi\PycharmProjects\DataWrangling\mn.csv', 'rb'))

mn_data = [d for d in mn_data_rdr]

def combine_data_dict(data_rows):
    data_dict = {}
    for row in data_rows:
        key = '%s-%s' % (row.get('HH1'), row.get('HH2'))
        if key in data_dict.keys():
            data_dict[key].append(row)
        else:
            data_dict[key] = [row]
    return data_dict

mn_dict = combine_data_dict(mn_data)

print len(mn_dict)