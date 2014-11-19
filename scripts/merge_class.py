#########################################################################################################
#
# This script joins MITE, Blastx and TEclass classifications and prints the final library in fasta format
# 
#########################################################################################################


from Bio import SeqIO
from Bio.Seq import Seq

teclass=open('all_Tes_80_200_TEclassified', 'r')   # Type here the name of the teclass classification file
blastx=open('all_TEs_80_200_blastx.txt', 'r')      # Type here the name of the blastx classification file
fasta=open('cryne_library_80_200.fasta', 'r')      # Type here the name of the file with elements in fasta
curated=open('cryne_lib.fasta', 'w')		   # Type is the name of an output file. Used again in lines 41 and 45

dic = {}


for line in teclass:
	line=line.strip()
	line=line.split('\t')
	a=str(line[0])
	a=a.strip()
	dic[a]=line[1]

for item in blastx:
	item=item.strip()
	item=item.split('\t')
	b=str(item[0])
	dic[b]=item[1]

	
for record in SeqIO.parse(fasta, 'fasta'): 
	record.id=record.id.strip()
	for k,v in dic.iteritems():
		if str(record.id) == str(k):
			curated.write('>'+str(k)+'#'+str(v)+'\n'+str(record.seq)+'\n')

curated.close()

clean=open('cryne_lib.fasta', 'r')	              # Reopen the file. Type again the same name as in line 14
out2=open('Cryne_lib.FINAL.fasta', 'w')	              # type here the name of the FINAL LIBRARY


for item in SeqIO.parse('cryne_lib.fasta', 'fasta'):  # Type here the same name of line 14
	name=str(item.id)
	seq=str(item.seq)
	seq=seq.replace('N', '')
	if 'MITE' in name:
		name=name.split('#')
		name2=name[0]+'#DNA/MITE'
		out2.write('>'+str(name2)+'\n'+str(seq)+'\n')
	else:
		out2.write('>'+str(name)+'\n'+str(seq)+'\n')
	
