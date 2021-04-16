def ORF(start_num,seq):
    for i in range(start_num-1, len(seq),3):
        if i != start_num-1:
            print(seq[i-3]+seq[i-2]+seq[i-1])
ORF(1, "GCTGGCGTCGAT")