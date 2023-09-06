```python
from bs4 import BeautifulSoup
import requests

class PaginationHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_page_content(self, page_number):
        url = f"{self.base_url}?page={page_number}"
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def get_total_pages(self, soup):
        pagination = soup.find('div', {'class': 'pagination'})
        if not pagination:
            return 1
        else:
            return int(pagination.find_all('a')[-2].get_text())
```
