blastn=open('LTRs_5copies.txt', 'r')
blastx=open('LTR.blastx.copies.txt', 'r')

biglist=[]


for line in blastn:
	line=line.strip()
	biglist.append(line)

for elto in blastx:
	elto=elto.strip()
	biglist.append(elto)

unicos=set(biglist)

for item in unicos:
	print item
