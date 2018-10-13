import os
import random
import csv

os.mknod('DbOfNames.csv')

last = open('CSV_Database_of_Last_Names.csv', 'r')
first = open('CSV_Database_of_First_Names.csv', 'r')

new = open('DbOfNames.csv','w')

firsts = tuple(csv.reader(first))
lasts = tuple(csv.reader(last))

names_written = []
for i in range(5500):
	first_name = random.choice(firsts)
	last_name = random.choice(lasts)
	if first_name not in names_written and last_name not in names_written:
		names_written.append(first_name)
		names_written.append(last_name)
		new.write(','.join(first_name+last_name+['\n']))

#---sort---
# print(os.getcwd())
# out = (os.system('sort -u DbOfNames.csv'))

first.close()
last.close()
new.close()
