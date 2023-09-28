```python
import json
from web_scraper_api.models.product import Product

def format_to_json(product: Product) -> str:
    """
    Formats a Product object into a JSON string.
    """
    product_dict = {
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "images": product.images
    }
    
    return json.dumps(product_dict)
```