import requests #getting content of the TED Talk page

from bs4 import BeautifulSoup #web scraping

import re #Regular Experession patern machine

# from urlib.requests import urlretrieve #download p4

import sys #for argument parsing 


#Exception Handling 

if len(sys.argv) > 1:
	url = sys.argv[1] 
else:
	sys.exit("Error: Please enter the TED Talk URL")

#url = "https://www.ted.com/talks/elizabeth_carlen_and_joanna_moles_how_pigeons_took_over_the_world"

#url = "https://www.ted.com/talks/christina_greer_gerrymandering_how_drawing_jagged_lines_can_impact_an_election"

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
	if(re.search("talkPage.init", str(val))) is not None:
		result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4), result").group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ....." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ...."  + file_name)


r = requests.get(mp4)

with open(file_name,'wb') as f:
	f.write(r.content)

#Alternate method
#urlretreive(mp4, file name)

print("Download Process finished")