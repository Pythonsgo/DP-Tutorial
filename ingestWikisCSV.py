# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) June 26, 2015

##########################################################################
## Imports
##########################################################################

import os
import csv

import requests
import bz2
from bz2 import decompress

import time

##########################################################################
## Module Constants
##########################################################################

DIRNAME = os.path.dirname(__file__)
DATAPATH = os.path.join(DIRNAME,'wikiFiles.csv')
field_names = ["Language", "Code", "Wiki", "Size", "Location", "Date"]

##########################################################################
## Modules
##########################################################################

# This function reads a CSV file and loads content into a dictionary.
def read_file_location(path, fieldnames):
	with open(path, 'rU') as data:
		reader = csv.DictReader(data, fieldnames = fieldnames)
		for row in reader:
			yield row			

# This function retrieves a bz2 compressed file based on a url and decompresses it.
def retrieve_bz2file(url):
	r = requests.get(url)
	xmlfile = bz2.decompress(r.content)
	return xmlfile
	
# This function stores a file in a specified storage location.
def store_file(path,xmlfile):
	with open(path, 'wb') as f:
		f.write(xmlfile)	

##########################################################################
## Program downloads, decompresses, and stores Wikipedia xml files for 
## 290 languages.  It uses the pages-articles-bz2 compressed files.
##########################################################################

if __name__ == "__main__":

	
	for idx, row in enumerate(read_file_location(DATAPATH, field_names)):
		if idx > 4: break
		
		#Determine start time of download
		start = time.clock()
	
		#Define the location of the language file to be downloaded
		url = "http://download.wikimedia.org/" + row["Wiki"] + row["Date"] + row["Location"]
				
		#Define the storage location for the downloaded and decompressed language file
		OUTPATH = "fixtures/" + row["Language"] + ".xml"
		
		#Retrieve, decompress, and store the language file
		store_file(OUTPATH,retrieve_bz2file(url))
		
		#Determine the download process time.
		elapsed = (time.clock()-start)
		
		#Provide elapsed time and confirm a successful download for each language.	
		print	
		print "The language file for %s has successfully been downloaded." % row["Language"]
		print "The download took %f seconds." %elapsed
		print
			
			

