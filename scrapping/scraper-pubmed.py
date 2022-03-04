from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://pubmed.ncbi.nlm.nih.gov/?term=anemia"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="full-docsum")

with open('health.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Author', 'Description']
    thewriter.writerow(header)

    for list in lists:
        title = list.find(
            'a', class_="docsum-title").text.replace('\n', '')
        author = list.find(
            'span', class_="docsum-authors full-authors").text.replace('\n', '')
        description = list.find(
            'div', class_="full-view-snippet").text.replace('\n', '')

        info = [title, author, description]
        thewriter.writerow(info)
