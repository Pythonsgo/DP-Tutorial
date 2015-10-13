# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015

##########################################################################
## Imports
##########################################################################
import re

import itertools
from itertools import product

import nltk
from nltk import word_tokenize

import numpy as np
import matplotlib.pyplot as plt

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
 

##########################################################################
## Modules
##########################################################################

def extract(path):
    with open(path, 'r') as f:

        # Store data for the current document
        current = {
            'id': None,
            'title': None,
            'url': None,
            'text': None,
        }
        
        

        # Read through the file, searching for doc tags
        for line in f:
            if DOCPAT.match(line):
                # We have a new document! Fetch the data from the line
                wid, url, title = DOCPAT.match(line).groups()

                # Initialize the new current document
                current['id']    = wid
                current['url']   = url
                current['title'] = title 
                current['text']  = ""

            elif CLOSE.search(line):
                # This is the end of a document
                CORPUS['text'] += current['text']
                yield current

            else:
                # Just append the text to the current text
                current['text'] += line
                
                
def plot_statistics(list1, list2):
    n_groups = 5
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    
    bar1 = plt.bar(index, list1, bar_width, 
                    alpha=opacity, 
                    color='b', 
                    label='Word Count')
                    
    bar2 = plt.bar(index, list2, bar_width, 
                    alpha=opacity, 
                    color='r', 
                    label='Vocabulary')
                    
    plt.xlabel('Percengate of Files')
    plt.ylabel('Number')
    plt.title('INSERT LANGUAGE Corpora Results')
    plt.xticks(index + bar_width, ('20%', '40%', '60%', '80%', '100%'))
    plt.legend()
    
    plt.tight_layout(True)
    plt.show()
                                    


##########################################################################
## Program 
##########################################################################

if __name__ == "__main__":
    
    document_count = 0
    vocab_count = []
    words_count = []
    
    for i,j in product(range(10), range(10)): 
            for doc in extract(file_name_stub + str(i) + str(j)):
                document_count += 1
            if i in [1,3,5,7,9] and j==9:
                #print i, j     
                raw = CORPUS['text'].decode('utf8')  
                tokens = word_tokenize(raw)
                counts = nltk.FreqDist(tokens)
                vocab = len(counts.keys())
                words = sum(counts.values())
                vocab_count.append(vocab)
                words_count.append(words)
                #print counts, vocab, words
                #print counts.most_common(100)
                
    #print document_count
    
    print vocab_count, words_count
    
    plot_statistics(words_count, vocab_count)
    
     
       
 