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
OUTPATH = os.path.join(DIRNAME, 'wikiDownloadInfo.csv')

field_names = ["Language", "Code", "Wiki", "Base_url", "Download_url", "Size"]
wiki_url = "https://dumps.wikimedia.org/backup-index.html"
wiki_stub = "https://dumps.wikimedia.org/"

##########################################################################
## Modules
##########################################################################

# This function reads a CSV file and loads content into a dictionary.
def read_file_location(path, fieldnames):
	with open(path, 'rU') as data:
		reader = csv.DictReader(data, fieldnames = fieldnames)
		for row in reader:
			yield row		
			
# This function takes a url for an html page and returns a beautiful soup object
def get_soup(url):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	return soup
	
#This function takes a url for the location of a wiki language list of downloads and
#returns the size of the download file and the url for the actual xml download files.
def find_download_location(url):
	soup = get_soup(url)
	info_list = []
	for link in soup.findAll("li", "file", "a"):
		if "pages-articles" in link.a["href"] and "-m" not in link.a["href"]: 
			info_dict = {"location": link.a["href"], "size": link.a.next.next}
			info_list.append(info_dict)		
	return info_list


	
##########################################################################
## Program takes list of wikipedia languages and obtains the url for the
## location of the back-up files for each language, the url of the location of the
## actual xml files to download, and their size and creates a CSV of this
##  information.
##########################################################################

if __name__ == "__main__":
	
	#Generate the list of all wiki project locations
	link_list = [link.get("href") for link in get_soup(wiki_url).findAll("a")]	

	
	#Create csv file for results
	with open(OUTPATH, 'wb') as f:
		dict_writer = csv.DictWriter(f, field_names)
	
		#Add the most current wiki project location for each language
		for idx, row in enumerate(read_file_location(DATAPATH, field_names)):
			for link in link_list:
				if row['Wiki'] + "/" in link and row['Wiki'][0]==link[0]:
					row['Base_url']=link
					info_list = find_download_location(wiki_stub+link+"/")
					for item in info_list:
						row['Download_url'] = item['location']
						row['Size'] = item['size']
						dict_writer.writerow(row)
					idx = idx + 1
			
				
		
		
		
		
			

