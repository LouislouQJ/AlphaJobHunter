import requests
import pandas as pd
from datetime import datetime,timedelta
from manage.config import config
import threading


class Crawler:
    def __init__(self):
        pass

    def if_contains(self, cut_obj, keyword_set):
        while True:
            try:
                if next(cut_obj) in keyword_set:
                    return True
            except StopIteration:
                return False

    def url_generator(self, page):
        pass

    def get_html(self, url):
        for i in range(1, 6):
            try:
                return requests.get(url)
            except:
                print("Access page failed, try %d times" % (i + 1))

    def single_page_crawler(self, page):
        pass

    def downloader_for_thread(self, page, temp_list_):
        temp_list_[page - 1] = self.single_page_crawler(page)
        pass

    def search_in_range(self, day_number):
        temp_list = [None] * config["MAX_PAGE_RANGE"]
        df = pd.DataFrame(columns=["Date", "Firms", "Url"])
        th_list = [threading.Thread(target=self.downloader_for_thread, kwargs={"page": i, "temp_list_": temp_list}) for
                   i in range(1, config["MAX_PAGE_RANGE"] + 1)]
        for i in th_list:
            i.start()
        for i in th_list:
            i.join()
        for i in temp_list:
            df = df.append(i)
        df["Date"] = df["Date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
        boundary = datetime.now() - timedelta(days=day_number)
        df = df[df["Date"] >= boundary]
        df = df.sort_values("Date", ascending=False)
        print("Scanning Done.")
        return df
