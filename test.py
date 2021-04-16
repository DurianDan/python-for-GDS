def get_ORF(seq,start_num):
    ORF = []
    for i in range(start_num-1, len(seq)-1,3):
        codon = seq[i-3]+seq[i-2]+seq[i-1]
        if codon == "TAA" or codon == "TAG" or codon == "TGA":
            break
        if start_num-1 != i:
            ORF.append(codon)
        if i+4 == len(seq):
            ORF.append(seq[i]+seq[i+1]+seq[i+2])  
    if "ATG" in ORF:
        return "".join(ORF[ORF.index("ATG"):])
    else:
        return "There's not start codon"
test =get_ORF("GCTGGCATGGTCGAAGGCGATGACGACGAAACCTTCCTTGGCCAGCGCCTCGCCATATAACACGTTCCCCGATGTT",1)
print(test)