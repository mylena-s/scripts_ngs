#!/usr/bin/env python

from Bio import SeqIO
import sys


def rename_desc(fasta_file, new_fasta,TAREAN_type, word):
    with open(fasta_file), open(new_fasta, "w") as new:
        for record in SeqIO.parse(fasta_file, "fasta"):
            record.id=record.id.split("_")[0]+TAREAN_type+"_"+record.id.split("_")[-1][:-2]
            record.id= word +"_"+ record.id
            SeqIO.write(record, new, "fasta")

if __name__ == "__main__":
    try:
        fasta_file=sys.argv[1]
        word=sys.argv[2]
        TAREAN_type=sys.argv[3]


    except:
        print ("Usage: rename_desc.py Fasta_file Prefix TAREAN_type")   

    new_fasta= fasta_file.split(".")[0] +"_renamed.fasta"
    rename_desc(fasta_file, new_fasta, TAREAN_type, word)


