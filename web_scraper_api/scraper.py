```python
import requests
from bs4 import BeautifulSoup
from .models.product import Product

def scrape_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return None
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return None
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    product_name = soup.find("span", attrs={"id":'productTitle'}).string.strip()
    price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    description = soup.find("div", attrs={'id':'productDescription'}).string.strip()
    images = [img['src'] for img in soup.find_all('img', {'class':'a-dynamic-image'})]

    product = Product(product_name, price, description, images)

    return product
```