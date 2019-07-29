"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

timeDict = {}
for exchange in calls:
    if exchange[0] in timeDict:
        timeDict[exchange[0]] += int(exchange[3])
    else:
        timeDict[exchange[0]] = int(exchange[3])
    if exchange[1] in timeDict:
        timeDict[exchange[1]] += int(exchange[3])
    else:
        timeDict[exchange[1]] = int(exchange[3])

longestTime = max(timeDict,key=lambda x:timeDict[x])
print(f'{longestTime} spent the longest time, {timeDict[longestTime]} seconds, on the phone during September 2016')
