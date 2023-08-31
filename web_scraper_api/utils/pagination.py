```python
from bs4 import BeautifulSoup
import requests

def handle_pagination(url):
    """
    Function to handle pagination in e-commerce websites
    """
    pages = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the pagination section
    pagination = soup.find('div', {'class': 'pagination'})

    if pagination:
        # Get all the links in the pagination section
        links = pagination.find_all('a')

        # Add the URL of each page to the pages list
        for link in links:
            page_url = link.get('href')
            if page_url not in pages:
                pages.append(page_url)

    return pages
```