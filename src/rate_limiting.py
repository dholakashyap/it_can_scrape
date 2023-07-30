```python
from flask_limiter import Limiter
from flask import Flask

app = Flask(__name__)

# Define the rate limits
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/scrape')
@limiter.limit("20 per minute")  # Limit the /scrape endpoint to 20 requests per minute
def scrape():
    # Scrape logic goes here
    pass

def get_remote_address():
    return request.remote_addr
```