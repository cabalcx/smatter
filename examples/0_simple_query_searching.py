from smatter.api import SMAT

s = SMAT()

TERM = 'qanon'

# post content from the TERM
qanon_content = s.content(term=TERM)
print(qanon_content)

# volume of content on the given sites
qanon_timeseries = s.timeseries(term=TERM)
print(qanon_timeseries)

# top users posting about the TERM
qanon_activity = s.activity(term=TERM)
print(qanon_activity)