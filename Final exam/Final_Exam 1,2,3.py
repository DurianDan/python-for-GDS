# create a dictionary from fasta files
'''FASTA_file = open(input("what is the file: "))
'''
FASTA_file = open("dna.example.fasta")
FASTA = FASTA_file.read().split("\n")
FASTA_file.close()
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

#each sequence in each record is a class Sequence
class Sequence:
    def __init__(self,record,seq,n,order):
        self.seq = seq
        self.repeats_len = n
        self.record = record
        self.order = order
    def order_in_record(self):
        return self.order
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
            ORF = "".join(ORF[ORF.index("ATG"):])
            return [len(ORF),self.seq.index("ATG"),ORF] 
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

#create multiple Sequence objects stored in class_sequences
class_sequences = []
repeats_length = input("What is the length of each repeats:")
for record in FASTA_dict:
    order = 0
    for sequence in FASTA_dict[record]:
        order += 1
        class_sequences.append(Sequence(record,sequence,repeats_length,order))

#get the max length of multiple unprocessed sequences
def compare_length():
    minormax = input("min or max ?: ")
    seqorORF = input("seq(seqence) or ORF ?: ")
    if seqorORF == "ORF":
        start_num = int(input("ORF 1 or 2 or 3 ?: "))
    #create a dictionary uncompared_lengths = (key:value) = (seq or ORF:lenghth of the key)
    uncompared_lengths = {}
    for obj in class_sequences:
        length = 0
        if seqorORF == "seq":
            length = obj.get_length()
        elif seqorORF == "ORF" and type(obj.get_ORF(start_num)) == list :
            length = obj.get_ORF(start_num)[0]
        if length != 0:
            uncompared_lengths.update({obj.get_name()+"__"+str(obj.order_in_record())+"__":length})
    #delete all keys with value 0, because those sequences don't have ORF
    #create a variable (compared_lengths) with max or min value in the dictionary (uncompared_lengths) 
    if minormax == "min":
        compared_length = min(list(uncompared_lengths.values()))
    elif minormax == "max":
        compared_length = max(list(uncompared_lengths.values()))
    compared_lengths = {}
    #get the key with max or min value
    for length in uncompared_lengths:
        if uncompared_lengths[length] == compared_length:
            compared_lengths.update({length:uncompared_lengths[length]})
    return compared_lengths
    