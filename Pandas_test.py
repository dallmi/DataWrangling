import pandas as pd
import os

base_dir = r'C:\Users\dallmi\PycharmProjects\DataWrangling'
filename1 = r'mn.csv'
filename2 = r'mn.csv'
in_path1 = os.path.join(base_dir,filename1)
in_path2 = os.path.join(base_dir,filename2)

df_data = pd.read_csv(in_path1)
df_header = pd.read_csv(in_path2)

df_data.head()

for row in df_data:
    print row

column1 = df_data['HH1'].tolist()

for a in column1:
    print a

column1.dtypes