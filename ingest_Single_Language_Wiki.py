# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) September 22, 2015

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
DATAPATH = os.path.join(DIRNAME,'wikiDownloadInfo.csv')
stub_url = "http://download.wikimedia.org/" 

#English for this example, but can be any of the 290 languages supported by Wikipedia
LANGUAGE = "English"

#Use for all languages other than English.
language_encoding = "Insert for language of interest here"

##########################################################################
## Modules
##########################################################################

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

			
	#Determine start time of download
	start = time.clock()
	
	#Define the location of the language file to be downloaded.  This one is specific to English
	url = stub_url + "/enwiki/latest/enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2"
	
	#For other language files it is based on the language encoding.  For example, Spanish (eswiki)
	#Must specify a number after articles if downloading a subdirectory.
	#url = stub_url + "/" + language_encoding + "/latest/" + language_encoding + "-latest-pages-articles.xml.bz2"
				
	#Define the storage location for the downloaded and decompressed language file
	OUTPATH = "fixtures/" + LANGUAGE + ".xml"
		
	#Retrieve, decompress, and store the language file
	store_file(OUTPATH,retrieve_bz2file(url))
		
	#Determine the download process time.
	elapsed = (time.clock()-start)
		
	#Provide elapsed time and confirm a successful download for each language.	
	print	
	print "The language file has been successfully downloaded."
	print "The download took %f seconds." %elapsed
	print
			
			

