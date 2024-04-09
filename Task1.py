"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = set()

for record in texts + calls:
    unique_numbers.add(record[0])  # Add incoming number
    unique_numbers.add(record[1])  # Add answering number

# Calculate the total count of unique telephone numbers
count = len(unique_numbers)

# Print the message
print(f"There are {count} different telephone numbers in the records.")
