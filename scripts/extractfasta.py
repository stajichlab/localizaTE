from Bio import SeqIO
from Bio.Seq import Seq


infile=open('libraryLTRs.txt', 'r')
infile2=open('Cryne_90.LTR.fasta', 'r')
outfile2=open('libraryLTRs.fasta', 'w')

recorrido=infile.readlines()


for record in SeqIO.parse(infile2, 'fasta'): 
	for line in recorrido:
		line=line.strip()
		if record.id == line:
			outfile2.write('>'+str(record.id)+'\n'+str(record.seq)+'\n')
			print record.id
