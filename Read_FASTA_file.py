#!/usr/bin/env python3
#the fasta file is Homo sapiens basigin (Ok blood group)
#from sys import argv
#FASTA_file = open(argv[1])
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
        dic[name] = ' '
    else:
        dic[list(dic.keys())[-1]] = dic[list(dic.keys())[-1]] +' '+ line

'''def print_dic():'''
print(dic)

