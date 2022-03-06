from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://pubmed.ncbi.nlm.nih.gov/?term=anemia"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="full-docsum")

with open('health.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['text']
    thewriter.writerow(header)

    for list in lists:
        text = list.find(
            'div', class_="full-view-snippet").text.replace('\n', '')

        info = [text]
        thewriter.writerow(info)
