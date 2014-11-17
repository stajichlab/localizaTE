from Bio import SeqIO
from Bio.Seq import Seq


genoma=open('Cryptococcus_neoformans_H99.unmasked.fasta', 'r') #  Type the name of input file
output=open('renamed_Cryptococcus_neoformans_H99.fasta', 'w')  #  Type the name of output file

x=0
for record in SeqIO.parse(genoma, 'fasta'): 
	x=x+1
	scaf=str(x)
	output.write('>scaffold_'+scaf+'\n'+str(record.seq)+'\n')
	print record.id+'..........lenght='+str(len(record.seq))
	
output.close()
genoma.close()
