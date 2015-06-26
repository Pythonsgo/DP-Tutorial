# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) June 26, 2015

##########################################################################
## Imports
##########################################################################

import os
import pandas as pd
import xlrd

import requests
import bz2
from bz2 import decompress

import time

##########################################################################
## Module Constants
##########################################################################

DIRNAME = os.path.dirname(__file__)
DATAPATH = os.path.join(DIRNAME,'wikiFiles.xlsx')


##########################################################################
## Program imports and decompresses wikipedia xml files for 290 languages.
##########################################################################

if __name__ == "__main__":
	#Import the file information as a dataframe.
	df = pd.read_excel(DATAPATH)

	#Download the files for all 290 languages in Wikipedia.  Temporarily set to five languages.
	for i in range(0,5):
		start = time.clock()
		
		#Use file input to determine location of the compressed language files.
		url = "http://download.wikimedia.org/"+df.loc[i,"Wiki"]+df.loc[i,"Date"]+df.loc[i,"Location"]
		
		language_name = df.loc[i,"Language"]
		
		#Request the compressed file and decompress the content.
		r = requests.get(url)

		xmlfile = bz2.decompress(r.content)

		#Set location and store decompressed files.
		OUTPATH = "fixtures/" + language_name + ".xml"

		with open(OUTPATH, 'wb') as f:
			f.write(xmlfile)
		
		#Determine the download time.
		elapsed = (time.clock()-start)
		
		#Provide elapsed time and confirm a successful download for each language.	
		print	
		print "The language file for %s has successfully been downloaded." % language_name
		print "The download took %f seconds." %elapsed
		print
		
		
		



