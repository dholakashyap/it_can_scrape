```python
import requests
from bs4 import BeautifulSoup
from .models.product import Product
from .utils.pagination import handle_pagination
from .utils.async_scraping import async_scrape
from .utils.error_handling import handle_error

class Scraper:
    def __init__(self, url, fields=None, pagination=False):
        self.url = url
        self.fields = fields
        self.pagination = pagination

    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            handle_error(err)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        product_data = self.extract_product_data(soup)
        
        if self.pagination:
            product_data += handle_pagination(soup, self.url, self.fields)
        
        return product_data

    def extract_product_data(self, soup):
        product_data = []
        products = soup.find_all('div', class_='product')

        for product in products:
            product_info = Product()

            if 'name' in self.fields:
                product_info.name = product.find('h2', class_='product-name').text

            if 'price' in self.fields:
                product_info.price = product.find('span', class_='product-price').text

            if 'description' in self.fields:
                product_info.description = product.find('p', class_='product-description').text

            if 'reviews' in self.fields:
                product_info.reviews = product.find('div', class_='product-reviews').text

            if 'ratings' in self.fields:
                product_info.ratings = product.find('div', class_='product-ratings').text

            if 'availability' in self.fields:
                product_info.availability = product.find('div', class_='product-availability').text

            product_data.append(product_info)

        return product_data
```