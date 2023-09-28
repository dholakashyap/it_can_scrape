```python
from flask import Flask
from web_scraper_api.api import scrape_product_data

app = Flask(__name__)
API_ENDPOINT = "/scrape"

@app.route(API_ENDPOINT, methods=['POST'])
def handle_request():
    return scrape_product_data()

if __name__ == "__main__":
    app.run(debug=True)
```