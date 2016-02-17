import urllib

# This module helps to navigate through html page objects
# http://stackoverflow.com/questions/29001307/going-through-html-dom-in-python
# http://www.crummy.com/software/BeautifulSoup/
# To install module use this command:
# $ pip install beautifulsoup4

from bs4 import BeautifulSoup

link = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/"
links = { link : [link]}

# Reading all urls with words
# This part is opens first page and populates the map with links

page = urllib.urlopen(link).read()
 
soup_page = BeautifulSoup(page, "html.parser").find('div', id='entries-selector')

tags_with_url = soup_page.find_all('a')

for tag in tags_with_url:
	links[tag['href']] = [tag['href']]

#
# print(len(links))

# now we are reading all pages for letter range
# exploring all links 
for link in links:	
	page = urllib.urlopen(link).read()
	soup_page = BeautifulSoup(page, "html.parser").find('div', id='paging')
	tags_with_url = soup_page.find_all('a')
	for tag in tags_with_url:
		links[link].append(tag['href'])
	
# print(links)
# running all links
for link_array in links:
	for link in links[link_array]:
		print(link)