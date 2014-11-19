
###########################################################################

#  Keeps the elements > 200 bp and cleans the headers of fasta sequences

###########################################################################

from Bio import SeqIO
from Bio.Seq import Seq


infile=open('cryne_library.fasta', 'r')                  # Type here the name of the infile
outfile=open('cryne_library_80_200.fasta', 'w')    # Type here the name of the outfile

for record in SeqIO.parse(infile, 'fasta'): 
	if len(record.seq) > 200:
		name=str(record.id)
		name=name.split(';seqs')
		name2=name[0]
		name2=name2.replace('centroid=', '')
		outfile.write('>'+str(name2)+'\n'+str(record.seq)+'\n')

