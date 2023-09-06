```python
import asyncio
from scraper import Scraper

class AsyncScraper:
    def __init__(self, urls, fields=None, pagination=False):
        self.urls = urls
        self.fields = fields
        self.pagination = pagination
        self.scraper = Scraper()

    async def scrape_url(self, url):
        return await self.scraper.scrape(url, self.fields, self.pagination)

    async def scrape_all(self):
        tasks = [self.scrape_url(url) for url in self.urls]
        return await asyncio.gather(*tasks)
```