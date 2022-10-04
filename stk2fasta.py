from Bio import AlignIO
import sys

if __name__ == "__main__":
    try:
        align_file=sys.argv[1]
    except:
        print ("Usage: sth2fasta.py align_file")   

    align = AlignIO.read(align_file, "stockholm")
    fasta = open(align_file+".fasta", "w")
    AlignIO.write(align, fasta, "fasta")
