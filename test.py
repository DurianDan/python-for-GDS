import os
direct_output = os.popen("elink -db gene -id 682 -target nuccore -name gene_nuccore_refseqrna | efetch -format fasta").read()
fasta = direct_output.split("\n")
while '' in fasta:
    fasta.remove('')
fasta_dict= {}
for line in fasta:
    if line[0]== '>':
        space = line.index(" ")
        name = line[1:space]
        fasta_dict[name] = list()
    value = fasta_dict[list(fasta_dict.keys())[-1]]
    if list(fasta_dict.keys())[-1] not in line:
        value = value.append(line)
print(fasta_dict)
