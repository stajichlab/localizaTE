#######################################
#script for cleaning headers
##########################################

lib=open('all_TEs_cryne', 'r')       # change here the input filename when necessary   


for line in lib:
	line=line.strip()
	if ';seqs=' in line:
		linef=line.strip()
		linef=linef.split(';seqs')
		linea=linef[0]
		linea=linea.strip()
		if 'centroid=' in linea:
			item=linea.replace('centroid=', '')
			print str(item)
		if 'RepeatScout' in linea:
			line=linea.split(' (')
			print str(line[0])
		elif 'Recon' in linea:
			line2=linea.split(' (')
			print str(line2[0])
	elif 'RepeatScout' in line:
			line=line.split(' (')
			print str(line[0])
	elif 'Recon' in line:
			line2=line.split(' (')
			print str(line2[0])
	elif 'MITE_' in line:
		lineg=str(line)
		lineg=line.strip()
		lineg=line.split(' ')
		linea2=lineg[0]
		print linea2
	else:
		print line

		
