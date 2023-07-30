```python
import asyncio
from scraper import scrape

async def async_scrape(urls, fields=None, pagination=False):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(scrape(url, fields, pagination))
        tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return responses
```