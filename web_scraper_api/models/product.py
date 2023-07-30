```python
class Product:
    def __init__(self, name, price, description, images):
        self.name = name
        self.price = price
        self.description = description
        self.images = images

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "images": self.images
        }
```