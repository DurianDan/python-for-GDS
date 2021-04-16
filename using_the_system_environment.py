#using sys module in terminal
import sys
sys.stdin.read() # take multiple input, "enter" after a input
#standard input: ctrl+D to exit input
sys.stdout.write("some useful input.\n")
#standard output: print out output and the length of output
sys.stderr.write("Warning: this input is not correct")
#standard error: print out error and the length of the string

import subprocess
#subprocess module interact with other program (in the same folder in which the running python file is)
#it lets use the process, give input or take output of the other program
subprocess.call(["/home/duriandan/learning/genomic data science/python for GDS/Read_FASTA_file.py","sequence.fasta"])
'''you'll have to put #!/usr/bin/env python3 
in the porgram that is trying to be read'''
