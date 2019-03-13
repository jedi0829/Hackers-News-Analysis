import pandas as pd
from dateutil.parser import parse
import read
data_hn = read.load_data()
def hour_extract(tstamp):
    time_holder = parse(tstamp, ignoretz=True)
    hour = time_holder.hour
    return hour
hour_submission = data_hn["submission_time"].apply(hour_extract)
hour_count = hour_submission.value_counts()
for name, row in hour_count.items():
    print("{0}:{1}".format(name, row))  