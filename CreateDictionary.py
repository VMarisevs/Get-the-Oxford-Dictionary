import urllib

# This module helps to navigate through html page objects
# http://stackoverflow.com/questions/29001307/going-through-html-dom-in-python
# http://www.crummy.com/software/BeautifulSoup/
# To install module use this command:
# $ pip install beautifulsoup4

from bs4 import BeautifulSoup

wordlist = {}

def main(start_link):

	#start_link = "http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/"
	links = { start_link : [start_link]}

	# Reading all urls with words
	# This part is opens first page and populates the map with links

	page = urllib.urlopen(start_link).read()
	 
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
			#print(link)
			parseHTML(link)

def parseHTML(link):
	page = urllib.urlopen(link).read()
	soup_page = BeautifulSoup(page, "html.parser").find('div', id='entrylist1')
	tags_with_url = soup_page.find_all('a')
	for tag in tags_with_url:
		# now it is ignoring non ASCII chars and makes all lowercase and splits into separate words
		words = tag.contents[0].encode('ascii',errors='ignore').lower().split()		
		for word in words:
			# print(word)
			# !ERROR! UnicodeEncodeError: 'charmap' codec can't encode character u'\u2019' in position
			# can't create a map with "o'clock" key
			# http://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python
			wordlist[word] = None

			
def writeMapToFile(words):
	file = open('words.txt', 'w')
	
	for word in words:
		file.write(word + "\n")
	file.close()
	
# main function explores all urls and then goes through and populates the word map
# and then writes whole map into file
if __name__ == "__main__":
	print "Sorry for delay, this scripts explores links, and parses html pages to get word list\n"
	links = [
		"http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/english/academic/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/american_english/academic/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/english/pictures/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/american_english/pictures/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/english/usage_notes/"
		,"http://www.oxfordlearnersdictionaries.com/wordlist/american_english/usage_notes/"
		]

	for link in links:
		print "exploring all sublinks in:\n\t " + link
		main(link)

	print "word map is created with " + str(len(wordlist)) + "words."

	writeMapToFile(wordlist)

	print("list of words saved into file")