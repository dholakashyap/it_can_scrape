```python
class Product:
    def __init__(self, name, price, description, reviews, ratings, availability):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = reviews
        self.ratings = ratings
        self.availability = availability

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "reviews": [review.to_dict() for review in self.reviews],
            "ratings": self.ratings,
            "availability": self.availability
        }
```