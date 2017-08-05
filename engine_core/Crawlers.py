import bs4 as bs
import pandas as pd
import jieba
from BaseCrawlers import Crawler


class Yingjiesheng(Crawler):
    def url_generator(self, page):
        return "http://www.yingjiesheng.com/commend-parttime-%d.html" % page

    def single_page_crawler(self, page):
        key_word = set(["证券", "银行", "基金", "资管", "资本"])
        url = self.url_generator(page)
        html = self.get_html(url)
        soup = bs.BeautifulSoup(html.content, "lxml")
        temp = soup.find_all("tr", {"class": "bg_0"})
        temp_list = []
        for i in temp:
            entity = i.find_all("td")
            if len(entity) >= 2:
                name = entity[0].text.replace("\n", " ")
                date = entity[1].text
                url = entity[0].find("a")["href"]
                url = "http://www.yingjiesheng.com" + url if url[0] == "/" else url
                words = jieba.cut(name, cut_all=True)
                if self.if_contains(words, key_word):
                    temp_list.append([date, name, url])

        df = pd.DataFrame(temp_list)
        df.columns = ["Date", "Firms", "Url"]
        return df


class Yingjiesheng_Shanghai(Crawler):
    def url_generator(self, page):
        return "http://www.yingjiesheng.com/shanghai-moreptjob-%d.html" % page

    def single_page_crawler(self, page):
        key_word = set(["证券", "银行", "基金", "资管", "资本"])
        url = self.url_generator(page)
        html = self.get_html(url)
        soup = bs.BeautifulSoup(html.content, "lxml")
        temp = soup.find_all("tr", {"class": "tr_list"})
        temp_list = []
        for i in temp:
            entity = i.find_all("td")
            if len(entity) >= 2:
                name = entity[0].text.replace("\n", "").strip()
                date = entity[1].text
                url = entity[0].find("a")["href"]
                url = "http://www.yingjiesheng.com" + url if url[0] == "/" else url
                words = jieba.cut(name, cut_all=True)
                if self.if_contains(words, key_word):
                    temp_list.append([date, name, url])

        df = pd.DataFrame(temp_list)
        df.columns = ["Date", "Firms", "Url"]
        return df


class Yingjiesheng_Beijing(Yingjiesheng_Shanghai):
    def url_generator(self, page):
        return "http://www.yingjiesheng.com/beijing-moreptjob-%d.html" % page


class Yingjiesheng_Shenzhen(Yingjiesheng_Shanghai):
    def url_generator(self, page):
        return "http://www.yingjiesheng.com/shenzhen-moreptjob-%d.html" % page
