# ========================================================= 8 Data Cleanup Standardizing and scripting

import dataset
db = dataset.connect('sqlite:///data_wrangling.db')
my_data_source = {
    'url':'http://www.tsmplug.com/football/premier-league-player-salaries-club-by-club/',
    'description':'Premier league Club Salaries',
    'topic': 'football',
    'verified': False,
}

table = db['data_sources']
table.insert(my_data_source)
another_data_source = {
    #'url':'http://www.premierleague.com/content/premierleague/en-gb/players/index.html',
    'url':'https://www.premierleague.com/stats/top/players/goals?se=54',
    'description':'Premier League Stats',
    'topic':'football',
    'verified':True,
}

table.insert(another_data_source)
sources = db['data_sources'].all()

print sources


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

#=========================================================================== Saving your data

import dataset
db = dataset.connect('sqlite:///data_wrangling.db')
table = db['unicef_survey']                                             # creates a new table

for row_num, data in enumerate(zipped_data):                           # we want to keep track what row we are on
    for question, answer in data:                                       # We know our data is broken into tuples, with our headers as a list in the first entry in the tuple and the responses
                                                                        # to those questions in the second part of the tuple. This code uses a for loop so we can parse and save the data contained therein.
        data_dict = {                                                   # Each question and answer has its own entry in our database, so we can join together all of the responses for each row (i.e. interview)
                                                                        # This code creates a dic with the necessary data for each response for each interview.
            'question': question[1],                                    # The plainly written question is the second entry in the list of the headers. This code saves that data as question
            'question_code': question[0],                                # saves short code of question
            'answer': answer,
            'response_number': row_num,                                 # To keep track of each row of responses / interview, this code includes the row_num from enumerate
            'survey':  'mn',
        }

        table.insert( )                                             # Finally, we insert our newly assembled dictionary into our db using our new table's insert method

# Test your data

import dataset

db = dataset.connect('sqLite:///data_wrangling.db')
wm_count = db.query('select count(*) from unicef_survey where survey="wm"')
count_result = wm_count.next()
print count_result