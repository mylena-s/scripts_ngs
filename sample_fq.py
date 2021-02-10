#!/usr/bin/env python3
import sys, os
from subprocess import call
from Bio import SeqIO
from count_bases_fasta import count_bases

def sample(n_reads, fastq_file, library_n, output_prefix):
    sample_command = "seqtk sample -s 666 "
    sample_input = fastq_file + " " + n_reads
    sample_output = output_prefix + "_" + library_n + ".subset.fastq"
    return sample_command + sample_input + " > " + sample_output

def concatenate(file1, file2, output_prefix):
    cat_command= "cat "+ file1 + " " + file2 + " > " + output_prefix+ "_concatenated.subset.fastq"
    return cat_command

def fastq_to_fasta(file, output_prefix):
    command= "seqtk seq -a " + file + " > " + output_prefix + "_concatenated.subset.fasta"
    return command

def rename_headers(fastq, library_n):
    original_file = fastq
    corrected_file = "corrected"+fastq

    with open(original_file) as original, open(corrected_file, "w") as corrected:
        for record in SeqIO.parse(original_file, "fastq"):        
            record.id = record.id +"_"+library_n
            SeqIO.write(record, corrected, "fastq")
    
def main(n_reads, fastq1, fastq2, output_prefix):
    print("Sampling "+n_reads+" reads from fastq1")
    call(sample(n_reads, fastq1, "1", output_prefix), shell=True)
    print("Sampling "+n_reads+" reads from fastq2")
    call(sample(n_reads, fastq2, "2", output_prefix), shell=True)
    rename_headers(output_prefix + "_1.subset.fastq", "1")
    rename_headers(output_prefix + "_2.subset.fastq", "2")
    print("Merging both subsamples of fastq files")
    call(concatenate("corrected" + output_prefix + "_1.subset.fastq" , "corrected" + output_prefix + "_2.subset.fastq", output_prefix), shell=True)
    print("Converting to fasta format")
    n_bases=str(count_bases(output_prefix+"_concatenated.subset.fastq", "fastq"))
    print("Total number of bases in file: "+n_bases)
    call(fastq_to_fasta(output_prefix + "_concatenated.subset.fastq", output_prefix+"_"+n_bases), shell=True)
    print("Removing temporary files")
    call(("rm "+ output_prefix+"_1.subset.fastq"), shell=True)
    call(("rm "+ output_prefix+"_2.subset.fastq"), shell=True)
    call(("rm "+ "corrected" + output_prefix +"_1.subset.fastq"), shell=True)
    call(("rm "+ "corrected" + output_prefix +"_2.subset.fastq"), shell=True)
    call(("rm "+ output_prefix+"_concatenated.subset.fastq"), shell=True)
    print("Done")
    
if __name__ == "__main__":
    try:
        n_reads = sys.argv[1]
        fastq1  = sys.argv[2]
        fastq2 = sys.argv[3]
        prefix = sys.argv[4]        
    except:
        print ("Lacking parameters. Usage: python3 sample_fq.py n_reads fastq1 fastq2 output_prefix")

    if type(int(n_reads)) != int:
        pass
    elif os.path.splitext(fastq1)[1] != ".fastq":
            sys.exit("File 1 with wrong extension")       
    elif os.path.splitext(fastq2)[1] != ".fastq":
            sys.exit("File 2 with wrong extension")
    else:
        main(n_reads, fastq1, fastq2, prefix)

