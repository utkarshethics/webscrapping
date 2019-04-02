from bs4 import BeautifulSoup
import urllib
import urllib.request
import certifi

IredditFile = urllib.request.urlopen("http://www.reddit.com", cafile=certifi.where())
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
