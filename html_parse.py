from html.parser import HTMLParser
import urllib
from BeautifulSoup import BeautifulSoup


#----------- HTMLParser implementation
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)]
#------------------------------


#Beautiful Soup implementation   -- ** Make sure ToS of website allow scraping**
#-------------------------
page = urllib.urlopen('www.website.com')
soup = BeautifulSoup(page)

x = soup.body.find('div', attrs={'class' : 'container'}).text
#--------------------------