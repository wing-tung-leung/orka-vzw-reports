#!/usr/bin/python

import sys

def getDescription(origin, comment):
	if origin == 'Petanque':
		return origin
	elif origin == '' and comment.lower().find('petanque') > -1:
		return 'Petanque'
	elif origin == 'Kaarters':
		return origin
	elif origin == '' and comment.lower().find('kaarter') > -1:
		return 'Kaarters'
	elif origin == 'Donderdagspelers' or comment.lower().find('seniorenpingpong') > -1:
		return 'Donderdagspelers'
	elif origin == 'IOCA':
		return origin
	elif origin == 'Huur gemeente':
		return origin
	else:
		txt = comment.replace('toogdienst dd', '').\
			replace('tapper', '').replace('Tapper', '')
		return origin + txt


for line in sys.stdin.readlines():
	fields = line.split(';')
	amount = fields[4]
	if amount[0] != '-':
		date = fields[0]
		tx = fields[1]
		origin = fields[2]
		comment = fields[3]
		description = getDescription(origin, comment)
		formattedLine = "%s;%s;%s;%s" % (date, description, tx, amount)
		sys.stdout.write(formattedLine)

