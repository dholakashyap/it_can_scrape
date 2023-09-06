```python
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    """
    Function to get HTML content of a webpage
    """
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def extract_data_field(soup, field):
    """
    Function to extract a specific data field from the HTML content
    """
    if field == 'Product Name':
        return soup.find('h1').text.strip()
    elif field == 'Product Price':
        return soup.find('span', {'class': 'price'}).text.strip()
    elif field == 'Product Description':
        return soup.find('div', {'class': 'description'}).text.strip()
    elif field == 'Customer Reviews':
        return [review.text.strip() for review in soup.find_all('div', {'class': 'review'})]
    elif field == 'Product Ratings':
        return soup.find('div', {'class': 'rating'}).text.strip()
    elif field == 'Product Availability':
        return soup.find('div', {'class': 'availability'}).text.strip()
    elif field == 'Product Images':
        return [img['src'] for img in soup.find_all('img', {'class': 'product-image'})]
    else:
        return None

def extract_data(soup, fields):
    """
    Function to extract all specified data fields from the HTML content
    """
    data = {}
    for field in fields:
        data[field] = extract_data_field(soup, field)
    return data
```