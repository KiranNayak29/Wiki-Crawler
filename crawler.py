from bs4 import BeautifulSoup
import requests
import time
response = requests.get("https://en.wikipedia.org/wiki/NBC")
resp = response.text
soup = BeautifulSoup(resp, 'html.parser')

mylinks=[]
link = soup.p.a.get("href")
link= "https://en.wikipedia.org"+link
time.sleep(5)
while (link not in mylinks) and ("psychology" not in link):
    mylinks.append(link)
    response = requests.get(link)
    resp = response.text
    soup = BeautifulSoup(resp, 'html.parser')
    link = soup.p.a.get("href")
    link = "https://en.wikipedia.org"+link
    print("\n {}  --  {}".format(soup.title.string,link))
    time.sleep(5)
