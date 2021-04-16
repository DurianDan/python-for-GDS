def usage():
    print ('processfasta.py : reads a FASTA file and builds a dictionary with all sequences bigger than a given length\nterminal> python3 processfasta.py [-h] [-1 <length>] <filename>\n-h print this message\n-1 <length> filter all sequences with a length smaller than <length> (default <length>=0)\n<filename> the file has to be in FASTA format')

import sys
from getopt import getopt

#o = optional, a = required arguments
# the ":" is added when the argument expects a value
o,a = getopt(sys.argv[1:], 'l:h')

opts = {}
seqlen = 0

#check for errors and help the user
for k,v in o:
    opts[k] = v
if '-h' in opts.keys():
    usage(), sys.exit()
if len(a) < 1 :
    usage()
    print(' ')
    sys.exit("input fasta file is missing")
if '-l' in opts.keys():
    if int(opts['l'])<0:
        print("the length of the sequence must be a positive interger")
        sys.exit()
    seqlen = opts['-l']


#open fasta file
FASTA_file = open(sys.argv[1])

#create sequence dictionary
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
print(dic)