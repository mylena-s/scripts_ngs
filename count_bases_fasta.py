#!/usr/bin/env python3
from Bio import SeqIO
import sys 

def count_bases(file, type="fasta"):
    '''counts the number of bases in all the sequences of a fasta file'''
    lenght=0
    for seq_record in SeqIO.parse(file, type):
        lenght= lenght + len(seq_record)
    return lenght



if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except:
        print ("Usage: count_bases.py Fasta_file")   
    print(count_bases(file))
