#https://bioinformatics.stackexchange.com/questions/15794/using-entrez-efetch-to-retrive-fasta-file-from-any-ncbi-database/15795#15795
import os
#os.system will paste anything in the coma to the terminal(UNIX) 
test = os.system("elink -db gene -id 682 -target nuccore -name gene_nuccore_refseqrna | efetch -format fasta")
#elink -db gene -id 682... will get direct to the gene desired
#efetch -format fasta will download the data in desired format
#each Entrez command can be queried by using | between commands

print(test)