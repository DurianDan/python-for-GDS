#this os.popen will capture the output from the OS shell and then stored in a varible
#(in a format that the user desired, inthis case, string)
import os
direct_output = os.popen("elink -db gene -id 682 -target nuccore -name gene_nuccore_refseqrna | efetch -format fasta").read()
FASTA = direct_output.split("\n")

#create a dictionary of sequences from the fasta variable
while '' in FASTA:
    FASTA.remove('')
FASTA_dict= {}
for line in FASTA:
    if line[0]== '>':
        space = line.index(" ")
        name = line[1:space]
        FASTA_dict[name] = list()
    value = FASTA_dict[list(FASTA_dict.keys())[-1]]
    if list(FASTA_dict.keys())[-1] not in line:
        value = value.append(line)