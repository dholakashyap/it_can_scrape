```python
class Review:
    def __init__(self, reviewer_name, review_text, review_rating):
        self.reviewer_name = reviewer_name
        self.review_text = review_text
        self.review_rating = review_rating

    def to_dict(self):
        return {
            "reviewer_name": self.reviewer_name,
            "review_text": self.review_text,
            "review_rating": self.review_rating
        }
```