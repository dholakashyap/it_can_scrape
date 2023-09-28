```python
from flask import Flask, request, jsonify
from .scraper import scrape_product_data
from .error_handler import handle_error
from .utils.request_validator import validate_request
from .utils.json_formatter import format_to_json

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        url = request.json['url']
        validate_request(url)
        product_data = scrape_product_data(url)
        json_response = format_to_json(product_data)
        return jsonify(json_response), 200
    except Exception as e:
        error_message = handle_error(e)
        return jsonify({'error': error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)
```