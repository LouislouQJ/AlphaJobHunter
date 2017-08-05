from Crawlers import *
from db_init import Jobs, session
from time import sleep


def run():
    crawlers = [Yingjiesheng_Beijing(), Yingjiesheng_Shanghai(), Yingjiesheng_Shenzhen()]
    for crawler in crawlers:
        df = crawler.search_in_range(30)
        for i in df.iterrows():
            if not session.query(Jobs).filter(Jobs.url == i[1].Url).all():
                session.add(Jobs(date=i[1].Date, firms=i[1].Firms, url=i[1].Url))
        session.commit()


if __name__ == '__main__':
    while True:
        run()
        sleep(24 * 3600)
