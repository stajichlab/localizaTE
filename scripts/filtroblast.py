
#############################################################

# Cleans the file parsed.blastx.output.txt. The output is a file with the name of the element and the classification 
# i.e =  H99/LTR_13_scaffold_3_1380375_1391054	LTR/Gypsy

#############################################################

blastx=open('parsed.blastx.output.txt', 'r')
output=open('all_TEs_80_200_blastx.txt', 'w')
for line in blastx:
	elto=line.strip()
	elto=line.split('\t')
	seq_blast=str(elto[0])
	hit=line.split('#')
	hit2=str(hit[1])
	hit_blast=hit2.split('_')[0]
	key=seq_blast
	value=str(hit_blast)
	output.write(str(key)+'\t'+str(value)+'\n')
