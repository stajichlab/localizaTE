##############################################################################################################
#
# This script prints the name of the LTR elements (consensus) with more than 5 hits > than 400 bp in a blastn 
#
##############################################################################################################

from collections import defaultdict

output=open('LTRs_5copies.txt', 'w')
infile=open('parsed.output', 'r')

lista=[]

def count_unsorted_list_items(items):
    counts = defaultdict(int)
    for item in items:
        counts[item] += 1
    return dict(counts)


for line in infile:
	line=line.strip()
	size=line.split('\t')
	if (int(size[5])-int(size[4])) > 400:   # You can change here the lenght cutoff  (400 bp)
		if float(size[-1]) > 90:
			lista.append(size[0])


for k, v in count_unsorted_list_items(lista).iteritems():
	if v>5:					 # You can change here the copy number cutoff (5 hits)
		output.write(str(k)+'\n')
