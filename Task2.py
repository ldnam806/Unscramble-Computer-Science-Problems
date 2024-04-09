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
# Dictionary to store total call durations for each telephone number
phone_time = {}
# Iterate through calls to calculate total call durations
for call in calls:
    timestamp = call[2]
    duration = int(call[3])
    month, year = timestamp.split()[0].split('-')[1], timestamp.split()[0].split('-')[2]
    if month == '09' and year == '2016':
        incoming_number, answering_number = call[0], call[1]
        # Add call duration to total for incoming number
        phone_time[incoming_number] = phone_time.get(incoming_number, 0) + duration
        # Add call duration to total for answering number (if different)
        if incoming_number != answering_number:
            phone_time[answering_number] = phone_time.get(answering_number, 0) + duration

# Find the telephone number with the longest total call duration
max_time_number = max(phone_time, key=phone_time.get)
total_time = phone_time[max_time_number]

# Print the message
print(f"{max_time_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")