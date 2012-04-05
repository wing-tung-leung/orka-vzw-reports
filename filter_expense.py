#!/usr/bin/python

import sys

def getDescription(destination, comment):
	if comment.find("DEELNAME IN DE ZICHTREKENINGKOSTEN") == 0:
		return "kosten rekening"
	elif comment.find("KOSTPRIJS BEHEER DEBETKAART") == 0:
		return "kosten debetkaart" 
	elif comment.find("DOORLOPENDE OPDRACHT 03871853") == 0:
		return "Lening"
	elif destination == 'O.R.K.A. VZW' and comment.find('spaar') >= 0:
		return None;
	else:
		return destination;

lineNumber = 0
for line in sys.stdin.readlines():
	lineNumber = lineNumber + 1
	fields = line.split(';')
	if line.strip() == "":
		continue
	if len(fields) != 5:
		sys.stderr.write('Field count = %i on line %i' % (len(fields), lineNumber))
		exit(1)
	amount = fields[4]
	if amount[0] == '-':
		date = fields[0]
		day = date.split('/')[0]
		month = date.split('/')[1]
		year = date.split('/')[2]
		simpleDate = "%s-%s" % (day, month)
		tx = fields[1]
		destination = fields[2]
		comment = fields[3][0:-1]  # get rid of special character
		sum = -1.0 * float(amount.replace(',', '.'))
		#print date
		description = getDescription(destination, comment)
		if (description == None):
			continue  # skip transfer savings account
		formattedLine = "%s;%s;%s;%.2f;%s\n" % (simpleDate, description, tx, sum, comment)
		#print amount
		#print " %.2f" % sum
		sys.stdout.write(formattedLine)

