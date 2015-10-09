#!/usr/bin/python

infile=open('TEclass.output', 'r')

for line in infile.readlines():
	if 'ID' in line:
		pass
	else:
		try:
			line=line.strip()
			line=line.split('\t')
			print str(line[1])+'\t'+str(line[2])
		except:
			pass
