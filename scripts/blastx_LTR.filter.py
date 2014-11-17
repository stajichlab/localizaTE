# -*- coding: utf-8 -*-

##################################################
#
#  Script for parsing blastx output file 
#
##################################################


import collections
from collections import OrderedDict
from collections import defaultdict

infile=open("blastx.output", 'r')
outfile=open("hits_summary", 'w')
outfile2=open("deleteme", 'w')
x=0
a=0
for line in infile.readlines():  ## Get only desired lines of the Blastn output
	if "Query=" in line:
		x=x+1
		outfile.write('HIT_'+str(x)+'\t'+line)
	if "0.0" in line:
		if 'Score =' in line:
			pass
		else:
			outfile.write('\t'+line)
	if "e-" in line:
		if 'Score =' in line:
			pass
		else:
			outfile.write('\t'+line)
	if 'No hits found' in line:
		outfile.write(line)

infile.close()
outfile.close()

infile2=open('prueba', 'r')

value=0				 #open dictionary using "defaultdict", which allows to use lists as values
dictionary=defaultdict(list)
key=0

for line in infile2.readlines():
	line=line.strip()
	if "Query=" in line:		# Lines with "hit" (name of query) are used as keys
		hit=line.strip()
		key=hit
		#print line
	else: 
		value=line
		dictionary[key].append(value)  # Appends every hit of each query into a list, used as value in the dictionary

od = collections.OrderedDict(sorted(dictionary.items()))
for k, v in od.iteritems(): 	#iterates over the dict, to show keys and values
	if '*' not in v[0]:
		outfile2.write(str(k)+'\n')

outfile2.close()
infile2.close()

fin=open("deleteme", 'r')
final=open('LTR.blastx.copies.txt', 'w')


for itm in fin:
	itm=itm.strip()
	itm=itm.split('Query= ')
	final.write(str(itm[1])+'\n')
	
