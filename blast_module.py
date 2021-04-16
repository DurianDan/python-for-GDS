from Bio.Blast import NCBIWWW
#Blast align the input sequence to the database, 
#NCBIWWW module provides web methods
fasta_string = open("sequence_1.fasta").read()
result_handle = NCBIWWW.qblast('blastn',"nt",fasta_string)


from Bio.Blast import NCBIXML
# NCBIXML module formats things more nicely
#providing multiple indexes to score the alignments
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        #hsps are the indexes to score the alignment
        if hsp.expect < E_VALUE_THRESH:
            print("***Alignment***")
            print("sequence: ", alignment.title)
            print("Length: ", alignment.length)
            print('e value: ', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
