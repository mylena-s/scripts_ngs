#!/usr/bin/env python3

import argparse
import sys, os
import csv
from Bio import SeqIO

def isolate_first_column(blast_output):
    blast_list=[]
    with open(blast_output) as blast:
        csv_reader = csv.reader(blast, delimiter='\t')
        for column in csv_reader:
            blast_list.append(column[0])
        return set(blast_list)
    
def remove_sequences(fasta_file, set_blast, new_fasta, new_fasta2):
    with open(fasta_file), open(new_fasta, "w") as new, open(new_fasta2, "w") as new2 :
        for record in SeqIO.parse(fasta_file, "fasta"):
            if record.id not in set_blast:
                SeqIO.write(record, new, "fasta")
            else:
                SeqIO.write(record, new2, "fasta")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script removes sequences found in a table's first column (such as query in blast output format 6)")
    parser.add_argument("-f", "--file", type=str, required=True, help="specify the fasta file", metavar="")
    parser.add_argument("-t", "--table", type=str, required=True, help="specify table or list with one seq id per line. If table is a blast .out must be format [6 qseqid qlen sseqid slen evalue bitscore length salltitles]", metavar="")

    #defining variables names
    args = parser.parse_args()
    fasta_file= args.file
    blast_output=args.blast
    new_fasta = fasta_file.split(".")[0]+"_blast.filtered.fasta"
    new_fasta2 = fasta_file.split(".")[0]+"_blast.removedseq.fasta"
    #running program
    set_blast=isolate_first_column(blast_output)
    remove_sequences(fasta_file, set_blast, new_fasta, new_fasta2)
                
                
        
    
