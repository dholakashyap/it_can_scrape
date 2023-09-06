```python
from flask import Flask, request, jsonify
from src.api import ScraperAPI
from src.error_handling import handle_errors

app = Flask(__name__)
api = ScraperAPI()

@app.route('/scrape', methods=['POST'])
@handle_errors
def scrape():
    data = request.get_json()
    url = data.get('url')
    fields = data.get('fields', [])
    pagination = data.get('pagination', False)
    async = data.get('async', False)
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    result = api.scrape(url, fields, pagination, async)
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
```