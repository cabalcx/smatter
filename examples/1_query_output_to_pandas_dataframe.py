from smatter.api import SMAT

# create API client
s = SMAT()

# establish a search term
TERM = 'qanon'

# timeseries of 'qanon' records 
df = s.timeseries(term=TERM,output='dataframe')

# print dataframe
print(df)