import argparse
import requests
from bs4 import BeautifulSoup

# from class

parser = argparse.ArgumentParser(description='Download information from E-Bay and covert it to JSON.')
parser.add_argument('search_term')
parser.add_argument('--num_pages', deafult=10)
args = parser.parse_args()
print('args.search_term=', args.search_term)

for page_number in range(1, int(args.num_pages)+1):
    # the ebay url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
    url += args.search_term
    url += '&_sacat=0&LH_TitleDesc=0&_pgn='
    url += str(page_number)
    url += '&rt=nc'
    print('url=', url)

    # download the html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)

    html = r.text
    
    # process the html
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select('.s-item__title')
    
    for tag in tags:
        items.append({
            'name': tag.text
        })
    
    print('len(items)', len(items))
