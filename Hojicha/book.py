import os
import requests
import re
import time
from database import SessionLocal
from utility import *
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc
from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, Boolean, func,update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from pytz import timezone

from database import Base, get_ulid,session
from logger import set_logger
from utility import now_timestamp
from database import Base, get_ulid,session


class BookItem(Base):
    ''' Bookテーブル用 '''
    __tablename__ = 'book'
    mysql_charset='utf8mb4',
    mysql_collate='utf8mb4_unicode_ci'
    
    id = Column('id', Integer, primary_key=True)
    title = Column('title',String(100),nullable=False)
    itemName = Column('itemName',String(20),nullable=False)
    itemPrice = Column('itemPrice',String(20),nullable=True)
  

#API
Rakuten_Ranking_API = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json"


class ProductScraping():
    ''' GoogleBooksAPIで本の情報を取得してDBに格納する '''
    #引数:データ型で指定できる。
    @staticmethod
    def fetch_items(keyword:str, max_results:int, page_count:int=1):
        item_list=[]
        params = {
            "q":keyword,
            "maxResults": max_results if max_results <= 40 else 40,
        }
        item_list = []
        
        # セッション開始
        db:Session = SessionLocal()
        for page in range(page_count):
            params["startIndex"] = page * max_results
            res = requests.get(Rakuten_Ranking_API,params=params)
            if res.status_code > 300:
                return item_list
            
            data = res.json()
            if not data.get("items"):
                return False
            for item in data.get("items"):
                try:
                    title = item["item"]["title"]
                except:
                    title = ""
                try:
                    itemName = item["item"]["itemName"]
                except:
                    itemName = ""
                try:
                    itemPrice = item["item"]["itemPrice"]
                except:
                    itemPrice = ""
                # try:
                #     authors = item["volumeInfo"]["authors"][0]
                # except:
                #     authors = ""

                # Insert
                db.add(BookItem(title=title, itemName=itemName, itemPrice=itemPrice))

        # 保存確定
        db.commit()
            
        return item_list

