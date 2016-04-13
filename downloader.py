from bs4 import BeautifulSoup
import urllib,urllib2
import os
from pytube import YouTube
from pprint import pprint

"""
	Make sure ffmpeg and 'pip install pytube'
	Python 2.7.10
	sudo easy_install BeautifulSoup4
	sudo easy_install pytube
"""


"""
def parseUrl(url):
	parts = url.split('/')
	if len(parts) == 6:
		return [parts[3], parts[4], parts[5]]
	else:
		return [parts[3], parts[4], '1']

def findAndDownloadImage(opener, url):
	manga, chapter, page = parseUrl(url)

	f = opener.open(url)
	html = f.read()
	soup = BeautifulSoup(html)

	image_src = soup.find('img',id='img')
	if image_src:
		image_src = image_src['src']
		image_type = image_src.split('.')[-1]

		directory = 'downloads/' + manga + '/' + chapter
		if not os.path.exists(directory):
				os.makedirs(directory)
		print directory + '/' + page + '.' + image_type
		image = open(directory + '/' + page + '.' + image_type, 'wb')
		image.write(opener.open(image_src).read())
		image.close()

def findNextPage(opener, url):
	html = opener.open(url).read()
	soup = BeautifulSoup(html)
	image = soup.find('img',id='img')
	if image:
		next_page = image.parent['href']
		return next_page
	else:
		return False
"""

def scrapeEventbrite():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	eventbriteURL = "http://www.eventbrite.com/e/alex-allyson-grey-dimond-saints-gaudi-michal-menert-bicycle-day-at-1015-folsom-tickets-23063378185"

	f = opener.open(eventbriteURL)
	html = f.read()
	soup = BeautifulSoup(html, "html.parser")

	summary = soup.find('span', class_='summary')
	summary = str(summary.getText())
	print summary

	location = soup.find('h2', class_='location')
	locationLinks = location.findAll('a')
	locationText = str(location.getText())

	if locationLinks:
		print "Found " + `len(locationLinks)` + (" link" if (len(locationLinks) == 1) else " links")
		locationLink = locationLinks[0]
		locationName = str(locationLink.getText()).strip()
		print "Location Name: " + locationName
		MAX_REPLACE = 1 # only remove the first occurrence of this
		locationAddress = locationText
		locationAddress = locationAddress.replace(locationName, '', MAX_REPLACE).strip()
		print locationAddress
	else:
		# TODO: do special handling to parse the location name from the address
		locationAddress = locationText

	dateTimeStart = soup.find('span', class_='dtstart').findChild('span', class_='value-title').get('title')
	dateTimeEnd = soup.find('span', class_='dtend').findChild('span', class_='value-title').get('title')
	print 'Date Start/End:', dateTimeStart, '  -  ', dateTimeEnd

	ticketTypes = soup.findAll('td', class_='ticket_type_name')
	ticketTypesList = []
	for ticketType in ticketTypes:
		# To get just the text, not text in sub tags:
		ticketTypeText = str(ticketType.find(text=True, recursive=False)).strip()
		ticketTypesList.append(ticketTypeText)
	print ticketTypesList

	prices = soup.findAll('td', class_='price_td')
	pricesList = []
	for price in prices:
		priceText = str(price.getText()).strip()
		pricesList.append(priceText)
	print pricesList


def scrapeYoutube():
	youtubeURL = "https://www.youtube.com/watch?v=Pe2Nu9whqDo"
	yt = YouTube(youtubeURL)
	video = yt.get('mp4', '360p')
	video.download('youtubeVideo.mp4')


if __name__=='__main__':

	scrapeEventbrite()
	scrapeYoutube()

"""
	type(locationLink)
	<class 'bs4.element.Tag'>
"""


"""
	findAndDownloadImage(opener, url)

	# find next page
	next_page = findNextPage(opener, url)
	while next_page:
		# set next_page to False if there is no next page aka when there is no <img id='img'
		next_page = findNextPage(opener, url)
		url = ROOT + next_page
		manga, chapter, page = parseUrl(url)
		findAndDownloadImage(opener, url)
		# print manga, chapter, page, "was saved!"
		pass

"""




