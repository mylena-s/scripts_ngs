#!/usr/bin/env python3
import sys, os
from subprocess import call
import pandas as pd



def read_table(table):
    df = pd.read_csv(table, sep="\t")
    return df

def rename_headers(old_name, new_name):
    call(("mv "+old_name+" "+new_name), shell=True)
    
def main(csv):
    df=read_table(csv)
    df.apply(lambda x: rename_headers(x.old_name, x.new_name), axis=1)
        
if __name__ == "__main__":
    try:
        csv = sys.argv[1]
                
    except:
        print ("Lacking parameters. Usage: python3 rename_csv.py csv_file. Csv file must contain the following headers: old_name new_name separated by tab")

    print("This script renames files irreversibly. Please, make sure you have a backup")
    i=input("Do you want to continue?: Y/N ")
    if i == "Y" or i == "y":
        main(csv)
    else:
        print("Canceled")
