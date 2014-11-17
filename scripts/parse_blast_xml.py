########################################

# Blast parser:
#
# Requires XML output (-m 7 flag) and '-parse_seqids' for keeping user IDs:
#
# Output:
#
# Query ID / hit_ID / query_start / query_end / hit_start / hit_end / e_value / num_identities / query_lengt / identity(%)

########################################


from Bio.Blast import NCBIXML
for record in NCBIXML.parse(open("blast.output.xml")) :
   for align in record.alignments :
       for hsp in align.hsps:
		l=len(hsp.query)
		perc=(float(hsp.identities)/float(l))*100
            	print str(record.query)+'\t'+str(align.hit_id)+'\t'+str(hsp.query_start)+'\t'+str(hsp.query_end)+'\t'+str(hsp.sbjct_start)+'\t'+str(hsp.sbjct_end)+'\t'+str(hsp.expect)+'\t'+str(hsp.identities)+'\t'+str(l)+'\t'+str(perc)
