```python
from flask import jsonify

def handle_error(e):
    response = {
        "error": str(e),
        "message": "An error occurred while processing your request. Please try again."
    }
    return jsonify(response), 500
```