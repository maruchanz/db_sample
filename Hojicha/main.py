from sqlalchemy.orm import Session

from book import *


if __name__=='__main__':
    res = ProductScraping.fetch_items(keyword="Python", max_results=40, page_count=10)
    print(res)
