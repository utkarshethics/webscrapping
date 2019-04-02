from bs4 import BeautifulSoup
import urllib2
import certifi
import request
redditfile = urllib2.urlopen("http://www.wise-moves.com", cafile=certifi.where())
reddithtml = redditfile.read()
redditfile.close()
#request.get(link, headers = {'User-agent': 'your bot 0.1'})
soup = BeautifulSoup(reddithtml, 'html.parser')
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print(links.get('href'))


