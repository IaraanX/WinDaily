import requests
from bs4 import BeautifulSoup



content = requests.get('https://uupdump.net/known.php')
soup = BeautifulSoup(content.text, 'html.parser')


href_list = []
text_list = []
uuid_list = []

for link in soup.find_all('a'):
    if (link.text[0:7] == "Windows"):
        href = link.get('href')
        text = link.text
        uuid = link.get('href')[20:]
        href_list.append(href)
        text_list.append(text)
        uuid_list.append(uuid)

