
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse

base_url = 'http://quotes.toscrape.com/'

authors_seen=set()

def clean(url):
    url=urljoin(base_url,url)
    path_url=urlparse(url).path
    clean_url=path_url.split('/')[2]
    return clean_url

def scrape_quote(html_soup):
    for i in html_soup.find_all('div',class_='quote'):
        data_quote=[]
        quote_text=i.find('span',class_='text').get_text(strip=True) if i else None
        quote_author_url=clean(i.find('small',class_='author').find_next_sibling('a').get('href'))
        tags=[]
        authors_seen.add(quote_author_url)
        for j in i.find_all('a',class_='tag'):
            quote_tag=j.get_text(strip=True) if j else None
            tags.append(quote_tag)
        data_quote.append({
            'Author':quote_author_url,
            'Qoute':quote_text,
            'Tags':tags
        })    

def scrape_author(author_soup,author_id):
    data_authors=[]
    author_name=author_soup.find('h3',class_='author-title')
    author_name=author_name.get_text(strip=True) if author_name else None
    author_dob=author_soup.find('span',class_='author-born-date')
    author_dob=author_dob.get_text(strip=True) if author_dob else None
    author_loc=author_soup.find('span',class_='author-born-location')
    author_loc=author_loc.get_text(strip=True) if author_loc else None
    author_des=author_soup.find('div',class_='author-description')
    author_des=author_des.get_text(strip=True) if author_des else None
    data_authors.append({
        'Author':author_name,
        'Date-Of-Birth':author_dob,
        'Location':author_loc,
        'Description': author_des
    })

url=base_url
while True:
    print("Now, Scraping Qoute-Page :",url) 
    r=requests.get(url)
    html_soup=BeautifulSoup(r.text,'html.parser')
    scrape_quote(html_soup)
    next_url=html_soup.select('li.next > a')
    if not next_url or not next_url[0].get('href'):
        break
    url=urljoin(base_url,next_url[0].get('href'))

for author_id in authors_seen:
    url=base_url +'/author/'+ author_id
    print("Now, Scraping Authors-Page :",url)
    r=requests.get(url)
    author_soup=BeautifulSoup(r.text,'html.parser')
    scrape_author(author_soup,author_id)

print("Done Scraping")