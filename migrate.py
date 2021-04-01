from Hojicha.database import Base,engine
from Hojicha.book import *  # 作成したいmodelsは必ずimportする

''' テーブル新規作成(migrate) '''

print("migrate開始")
Base.metadata.create_all(bind=engine)