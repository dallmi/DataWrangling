import os

def replace_list(lst, search_term, replace_with):
    """# replace values in existing list from i.e. S01 to S02 etc."""
    new_list = []
    for idx, item in enumerate(lst):
        if search_term in item:
            item = str.replace(item, search_term, replace_with)
            new_list.append(item)
    return new_list



lst_S1 = ['S01E01','S01E02','S01E03','S01E04','S01E05','S01E06','S01E07','S01E08','S01E09','S01E10','S01E11','S01E12','S01E13',
          'S01E14','S01E15','S01E16','S01E17','S01E18','S01E19','S01E20','S01E21','S01E22','S01E23','S01E24','S01E25','S01E26']
lst_S2 = lst_S1
lst_S3 = lst_S1
dict_S3_alternative = {'301' : 'S3E01', '302' : 'S3E02' ,'303' : 'S3E03' ,'304' : 'S3E04' ,'305' : 'S3E05' ,'306' : 'S3E06' ,'307' : 'S3E07' ,
                      '308' : 'S3E08' ,'309' : 'S3E09' ,'310' : 'S3E10' ,'311' : 'S3E11' ,'312' : 'S3E12' ,'313' : 'S3E13' ,'314' : 'S3E14' ,'315' : 'S3E15' ,'316' : 'S3E16',
                      '317' : 'S3E17' ,'318' : 'S3E18' ,'319' : 'S3E19' ,'320' : 'S3E20' ,'321' : 'S3E21' ,'322' : 'S3E22' ,'323' : 'S3E23' ,'324' : 'S3E24' ,'325' : 'S3E25' ,'326' : 'S3E26'}
lst_S4 = lst_S1
lst_S5 = lst_S1
lst_S6 = lst_S1
lst_S7 = lst_S1
lst_S8 = lst_S1
lst_S9 = lst_S1
lst_S10 = lst_S1

lst_S2 = replace_list(lst_S1, 'S01', 'S02')
lst_S3 = replace_list(lst_S1, 'S01', 'S03')
lst_S4 = replace_list(lst_S1, 'S01', 'S04')
lst_S5 = replace_list(lst_S1, 'S01', 'S05')
lst_S6 = replace_list(lst_S1, 'S01', 'S06')
lst_S7 = replace_list(lst_S1, 'S01', 'S07')
lst_S8 = replace_list(lst_S1, 'S01', 'S08')
lst_S9 = replace_list(lst_S1, 'S01', 'S09')
lst_S10 = replace_list(lst_S1, 'S01', 'S10')
lst = lst_S1+lst_S2+lst_S3+lst_S4+lst_S5+lst_S6+lst_S7+lst_S8+lst_S9+lst_S10



Season_Name = 'Mike & Molly_'
rootdir = r'\\WDMYCLOUD\Public\Shared Videos\02 comedy\Mike und Molly\Staffel 4'
for subdir, dirs, files in os.walk(rootdir):
#    for episode, v in dict_S3_alternative.iteritems():
    for episode in lst:
        for file in files:
            file_format = file[len(file)-4:]
            if episode in (file).upper():
                filepath_old = subdir + os.sep + file
            #   fname_new = Season_Name + v + file_format
                fname_new = Season_Name + episode + file_format
                filepath_new = os.path.join(subdir, fname_new)
                print filepath_new
                os.rename(filepath_old, filepath_new)


