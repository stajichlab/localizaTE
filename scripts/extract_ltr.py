
######################################################################################################

#  Program for extracting full-lenght LTRs from the ltrharvest output. 
#  Chanche the name of the assembly file in the "genoma" label. Sequences must be named as scaffold_1

#######################################################################################################


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqFeature import SeqFeature, FeatureLocation

genoma='renamed_Cryptococcus_neoformans_H99.fasta'   # Type here the name of the input file
infile=open('ltrharvest.out', 'r')
outfile1=open('listaLTR', 'w')
outfile2=open('LTRs.fasta', 'w')

def filtrar(filename):
	for line in filename.readlines():
		if '#' in line:
			pass
		else:
			dividir=line.split('  ')
			scaffold=int(dividir[-1])+1
			inicio=dividir[0]
			final=dividir[1]
			outfile1.write('scaffold_'+str(scaffold)+'\t'+inicio+'\t'+final+'\n')

filtrar(infile)

outfile1.close()

ltr=open('listaLTR', 'r')

recorrido=ltr.readlines()
x=0
for line in recorrido:
	line=line.strip()
	line=line.split('\t')
	start=int(line[1])
	end=int(line[2])
	#print end-start
	x=x+1
	for record in SeqIO.parse(genoma, 'fasta'):  
		if record.id == str(line[0]):
			print '>'+'LTR_'+str(x)+'_'+record.id+'_'+str(start)+'_'+str(end)
			outfile2.write('>'+'LTR_'+str(x)+'_'+str(record.id)+'_'+str(start)+'_'+str(end)+'\n'+str(record.seq[start:end])+'\n')

ltr.close()
outfile2.close()
