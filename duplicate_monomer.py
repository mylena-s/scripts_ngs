#!/usr/bin/python3

import sys, os
from Bio import SeqIO
import argparse

def manipulate_files(fasta):
    return fasta, "duplicated_" + fasta

def duplicate_monomer(fasta, n):
    original_file, duplicated_file = manipulate_files(fasta)

    with open(original_file), open(duplicated_file, "w") as duplicated:
        for record in SeqIO.parse(original_file, "fasta"):        
            record.seq = record.seq * n
            SeqIO.write(record, duplicated, "fasta")

def achieve_lenght(fasta, lenght):
    original_file, duplicated_file = manipulate_files(fasta)
    with open(original_file), open(duplicated_file, "w") as duplicated:
        for record in SeqIO.parse(original_file, "fasta"):        
            while len(record.seq)< lenght:
                record.seq = record.seq + record.seq
        SeqIO.write(record, duplicated, "fasta")
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script duplicates N times each record inside a fasta file", epilog= "contact: mylena.santander@usp.br")
    parser.add_argument("-f", "--file", type=str, required=True, help="specify the fasta file", metavar="")
    parser.add_argument("-n", "--number", type=int, default= 2, help="number of times to duplicate monomer (default =2)", metavar="")
    parser.add_argument("-t", "--type", type=int, default= 1, choices= [1, 2], help="running mode: 1= duplicate n times (used with -n), 2=duplicate to reach lenght (used with -l)", metavar="")
    parser.add_argument("-l", "--lenght", type=int, default=1, help="specify the minimun lenght that you want to achieve by duplicating", metavar="")

    args = parser.parse_args()
    fasta  = args.file
    n = args.number
    mode = args.type
    lenght = args.lenght
    
    if mode == 1:
        duplicate_monomer(fasta, n)
    else:
        if lenght == 1:
            print("Monomer will not be duplicated since no lenght was specified")
        else:
            achieve_lenght(fasta, lenght)
    print("Done! Thanks!")
