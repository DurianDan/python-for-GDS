def has_stop_codons(SEQ,seq_type):
    """check if the seq has stop-codons, 2nd argument is the start of the read
    2nd argument is 0 by default"""
    SEQ = SEQ.upper()
    if seq_type is "rna":
        stop_codons = ("UAA","UAG","UGA")
        for i in range(0,len(SEQ),3):
            if SEQ[i:i+3] in stop_codons:
                return "Yes, it is"
            else: 
                return "No, duh!"
    if seq_type is "dna":
        seq_order = input("Is it 5to3 or 3to5? ")
        if seq_order is "3to5":
            stop_codons = ("ATT","ATC","ACT")
            for i in range(0,len(SEQ),3):
                if SEQ[i-3:i] in stop_codons:
                    return "Yes, it is"
                else: 
                    return "No, duh!"
        if seq_order is "5to3":
            stop_codons = ("TAA","TAG","TGA")
            for i in range(0,len(SEQ),3):
                if SEQ[i-3:i] in stop_codons:
                    return "Yes, it is"
                else: 
                    return "No, duh!"

print(has_stop_codons("juaajjjjjjj","dna"))