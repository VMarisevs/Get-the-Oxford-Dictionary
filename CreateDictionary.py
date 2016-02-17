import urllib

# This module helps to navigate through html page objects
# http://stackoverflow.com/questions/29001307/going-through-html-dom-in-python
# http://www.crummy.com/software/BeautifulSoup/
# To install module use this command:
# $ pip install beautifulsoup4

from bs4 import BeautifulSoup

link = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/"
links = []

# Reading all urls with words
#
page = urllib.urlopen(link).read()
 
soup_page = BeautifulSoup(page, "html.parser").find('div', id='entries-selector')

tags_with_url = soup_page.find_all('a')

for tag in tags_with_url:
	links.append(tag['href'])

print(links)
print(len(links))
