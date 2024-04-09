"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
# Load calls data from 'calls.csv'
outgoing_calls = set()
incoming_calls = set()
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        outgoing_calls.add(row[0])
        incoming_calls.add(row[1])

# Load texts data from 'texts.csv'
outgoing_texts = set()
incoming_texts = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        outgoing_texts.add(row[0])
        incoming_texts.add(row[1])

# Identify potential telemarketers
potential_telemarketers = outgoing_calls - (outgoing_texts | incoming_texts | incoming_calls)

# Print potential telemarketers
print("These numbers could be telemarketers:")
for number in sorted(potential_telemarketers):
    print(number)