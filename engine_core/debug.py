from Crawlers import *
from sqlalchemy.orm import sessionmaker
from db_init import engine, Jobs

Session = sessionmaker(engine)
session = Session()
a = Yingjiesheng_Shanghai()
df = a.search_in_range(3)
for i in df.iterrows():
    if not session.query(Jobs).filter(Jobs.url == i[1].Url).all():
        session.add(Jobs(date=i[1].Date, firms=i[1].Firms, url=i[1].Url))
session.commit()
q = session.query(Jobs).all()
