# coding: utf-8
import requests
import time
from scrapy import Selector
import os


class XiaoHuaSpider(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    def spider(self):
        """
        爬虫入口
        :return:
        """
        url = "http://www.xiaohuar.com/hua/"
        response = requests.get(url, headers=self.headers)
        selector = Selector(text=response.text)
        total_pages = selector.css(".page_num a")[-1:].css("::attr(href)").re(r".*?(\d+).html")[0]  # 总页数
        self.parse_html(selector)  # 第一页爬取

        for page in range(1, 5):  # 第二页至第五页
            url = f"http://www.xiaohuar.com/list-1-{page}.html"
            response = requests.get(url, headers=self.headers)
            selector = Selector(text=response.text)  # 创建选择器
            self.parse_html(selector)  # 解析网页

    def parse_html(self, selector):

        img_list = selector.css(".item_list.infinite_scroll .item_t .img")
        for img in img_list:
            title = img.css("a img ::attr(alt)").extract_first("")
            src = img.css("a img ::attr(src)").extract_first("")

            if "file" in src:  # 第一个图片和其他图片地址不一样
                src = "http://www.xiaohuar.com" + src
            img_res = requests.get(src, headers=self.headers)
            data = img_res.content
            self.save_img(title, data)

    @staticmethod
    def save_img(title, data):
        """
        保存图片到本地
        :param title:
        :param data:
        :return:
        """
        os.chdir("D:\\测试\\校花")   # 需要先在本地创建此目录
        if os.path.exists(title + ".jpg"):
            print(f"{title}已存在")
        else:
            print(f"正在保存{title}")
            with open(title + ".jpg", "wb")as f:
                f.write(data)

if __name__ == '__main__':
    spider = XiaoHuaSpider()
    t1 = time.time()
    spider.spider()
    t2 = time.time()
    print(t2 - t1)
