# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015

##########################################################################
## Imports
##########################################################################

import re

import itertools
from itertools import product



##########################################################################
## Module Constants
##########################################################################


 # Match patterns like <doc id="7" url="https://es.wikipedia.org/wiki?curid=7" title="Andorra">
DOCPAT = re.compile(r'^<doc id="(\d+)" url="(.+)" title="(.+)">$', re.I)
CLOSE  = re.compile(r'^</doc>$', re.I)

file_name_stub = 'wiki_'

CORPUS = {
    'text': "",
}
 
LANGUAGE = "Insert Language Name Here"
file_store_stub = LANGUAGE+"SK"

##########################################################################
## Modules
##########################################################################

def extract(path):
    with open(path, 'r') as f:

        # Store data for the current document
        current = {
            'text': None,
        }     

        # Read through the file, searching for doc tags
        for line in f:
            if DOCPAT.match(line):
                # Initialize the new current document
                current['text']  = ""

            elif CLOSE.search(line):
                # This is the end of a document
                CORPUS['text'] += current['text']
                yield current

            else:
                # Just append the line to the current text after eliminating
                # capital letters, punctuation, and numbers.
                line = line.lower()
                line = "".join(c for c in line if c not in ('!', '.', ',', ')', '(','?', '"'))
                line = "".join(c for c in line if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
                current['text'] += line
                
  
def store(path, text):
    with open(path, 'a') as f:
        f.write(text)             
                


##########################################################################
## Program combines text from multiple documents in each of the files
## generated by the WikiExtractor and writes them to a single file to be
## used for machine learning.
##########################################################################

if __name__ == "__main__":
    
    document_count = 0

    
    for i,j in product(range(10), range(10)): 
            for doc in extract(file_name_stub + str(i) + str(j)):
                document_count += 1
            OUTPATH = LANGUAGE + "/"+ file_store_stub + str(i) + str(j) + ".txt"
            store(OUTPATH, CORPUS['text'])
            CORPUS['text'] = ""  
                
                
    print document_count
    
 
     
       
 