# create a dictionary from fasta files
FASTA_file = open(input("what is the file: "))
FASTA = FASTA_file.read().split("\n")
FASTA_file.close()
while '' in FASTA:
    FASTA.remove('')
dic = {}
for line in FASTA:
    if line[0]== '>':
        space = line.index(" ")
        name = line[1:space]
        dic[name] = ''
    else:
        dic[list(dic.keys())[-1]] = dic[list(dic.keys())[-1]] +' '+ line

class Sequence:
    def __init__(self,record,seq,n):
        self.seq = seq
        self.repeats_len = n
        self.record = record
    def get_name(self):
        return self.record
    def get_length(self):
        return len(self.seq)
    def get_ORF(self,start_num):
        ORF = []
        for i in range(start_num-1, len(self.seq)-1,3):
            codon = self.seq[i-3]+self.seq[i-2]+self.seq[i-1]
            if codon == "TAA" or codon == "TAG" or codon == "TGA":
                break
            if start_num-1 != i:
                ORF.append(codon)
            if i+4 == len(self.seq):
                ORF.append(self.seq[i]+self.seq[i+1]+self.seq[i+2])  
        if "ATG" in ORF:
            return "".join(ORF[ORF.index("ATG"):])
        else:
            return "There's not start codon"
    def get_repeats(self):
        from collections import Counter
        bases_3 = []
        for i in range(0,len(self.seq)+1):
            if i+self.repeats_len == len(self.seq):
                break
            if i+self.repeats_len != len(self.seq):
                bases_3.append(self.seq[i:i+self.repeats_len])
        bases_3 = dict(Counter(bases_3))
        repeats = dict()
        for keys in bases_3:
            if bases_3[keys] != 1:
                repeats[keys] = bases_3[keys]
        return repeats
    def max_occurences(self):
        repeats_dict = self.get_repeats()
        max_occ_rate = max(repeats_dict.values())
        dict_max_occ = dict()
        for i in repeats_dict:
            if repeats_dict[i] == max_occ_rate:
                dict_max_occ.update({i:max_occ_rate})
        return dict_max_occ

print(dic)