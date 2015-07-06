# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) July 5, 2015

##########################################################################
## Imports
##########################################################################

import os
import csv

from BeautifulSoup import BeautifulSoup
import urllib2



##########################################################################
## Module Constants
##########################################################################

DIRNAME = os.path.dirname(__file__)
DATAPATH = os.path.join(DIRNAME,'wikiFilesUpdate.csv')
OUTPATH = os.path.join(DIRNAME, 'wikiFileCurrent.csv')

field_names = ["Language", "Code", "Wiki", "Base_url"]
wiki_url = "http://dumps.wikimedia.org/backup-index.html"

##########################################################################
## Modules
##########################################################################

# This function reads a CSV file and loads content into a dictionary.
def read_file_location(path, fieldnames):
	with open(path, 'rU') as data:
		reader = csv.DictReader(data, fieldnames = fieldnames)
		for row in reader:
			yield row		
			
# This functions takes a url for an html page, parses it, and prints a list of all the links
def find_link_list(url):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	link_list = [str(link.get("href")) for link in soup.findAll("a")]
	return link_list

	
##########################################################################
## Program takes list of wikipedia languages and obtains the url for the
## location of the back-up files for each language and creates a CSV with this information
##########################################################################

if __name__ == "__main__":
	
	#Generate the list of all wiki project locations
	link_list = find_link_list(wiki_url)
	
	#Create csv file for results
	with open(OUTPATH, 'wb') as f:
		dict_writer = csv.DictWriter(f, field_names)
	
		#Add the most current wiki project location for each language
		for idx, row in enumerate(read_file_location(DATAPATH, field_names)): 
			for link in link_list:
				if row['Wiki'] + "/" in link and row['Wiki'][0]==link[0]:
					row['Base_url']=link
					dict_writer.writerow(row)
					idx = idx + 1
			
				
		
			
	
			
			

