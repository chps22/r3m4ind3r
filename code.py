#!/bin/env python3
import csv
import datetime

#open data.csv and process using today to obtain today's work/tasks
with open('/home/sunny/r3m4ind3r/data.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	today = datetime.datetime.today()
	today = today.strftime("%Y-%m-%d")
	for row in csv_reader:
		if row[0] == today:
			date = row[0]
			subject = row[1].replace(' ', '_')
			topic = row[2].replace(' ', '_')

#print the values to stdout
print(date)
print(subject)
print(topic)
