"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
from functools import reduce

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#Filter for calls from Bangalore numbers
bangaloreExchanges = list(filter(lambda x: x[0][:5] == '(080)', calls))
codes = {}

for exchange in bangaloreExchanges:
    #Fixed Lines
    if exchange[1][0] == '(':
        if re.match(r"\(([0-9]+)\)", exchange[1]).group(0)[1:-1] in codes:
            codes[re.match(r"\(([0-9]+)\)", exchange[1]).group(0)[1:-1]] += 1
        else:
            codes[re.match(r"\(([0-9]+)\)", exchange[1]).group(0)[1:-1]] = 1 
    #Telemarketers 
    elif exchange[1][:3] == '140':
        if '140' in codes:
            codes['140'] += 1
        else:
            codes['140'] = 1
    #Mobile Numbers
    else:
        if exchange[1][:4] in codes:
            codes[exchange[1][:4]] += 1
        else:
            codes[exchange[1][:4]] = 1

print("The numbers called by people in Bangalore have codes:")
for code in sorted([*codes]):
    print(code)
fixedLines = codes['080']
allLines = reduce(lambda x, value: x+value, codes.values(), 0)
print(f"{round(fixedLines*100/allLines,2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


