from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep
from lxml import etree
from get_spuId import spuId_spider
from comment_spider import comment_spider


class vip_spider():
    def __init__(self, keyword, path):
        self.keyword = keyword
        self.path = path
        option = ChromeOptions()
        option.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')  # 设置无头浏览器
        self.bro = webdriver.Chrome(options=option)
        self.bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
        })

    def start(self):
        url = "https://category.vip.com/suggest.php?keyword=%s" % self.keyword
        self.bro.get(url)
        html = etree.HTML(self.bro.page_source)
        try:
            pages = html.xpath("//*[@id='J_pagingCt']/a")[-2].text
        except:
            pages = html.xpath('//*[@id="J_pagingCt"]/span[@class="total-item-nums"]')[0].text[1:-1]
        print("共" + pages + "页商品，开始爬取...")
        prod_ids = ""
        # self.bro.quit()
        for i in range(1, int(pages) + 1):
            print("等待3秒...")
            sleep(3)
            print("获取第" + str(i) + "页商品ID...")
            url = "https://category.vip.com/suggest.php?keyword=%s&page=%d" % (self.keyword, i)
            prod_list = self.load_data(url)
            count = 1

            lists = []

            while len(prod_list) >= 50:
                tl = prod_list[0:50]
                lists.append(tl)
                prod_list = prod_list[50:]
            lists.append(prod_list)

            for prod_list in lists:
                prod_ids = ','.join(prod_list)
                sp = spuId_spider(keyword=self.keyword, prod_ids=prod_ids)
                spuIds = sp.getIds()
                print("------------------------------------")
                print("开始爬取商品评论......")
                for spuId in spuIds:
                    print("开始爬取第" + str(count) + "个商品评论")
                    Spider = comment_spider(spuId, self.path)
                    Spider.main()
                    count += 1
        self.bro.quit()
        return prod_ids

    def load_data(self, url):
        self.bro.get(url)
        self.bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏
        self.bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏
        sleep(5)
        prod_ids = self.parser_data()
        return prod_ids

    def parser_data(self):
        html = etree.HTML(self.bro.page_source)
        div_list = html.xpath('//section[@class="goods-list c-goods-list--normal"]/div')[1:]
        pro_list = []
        for div in div_list:
            # sleep(0.5)
            # dic={}
            # try:
            #     dic["title"]=div.xpath('.//div[@class="c-goods-item__name  c-goods-item__name--two-line"]/text()')[0]
            # except:
            #     dic["title"]=""
            # try:
            #     dic["sale_price"]=div.xpath('.//div[@class="c-goods-item__sale-price J-goods-item__sale-price"]//text()')[1]
            # except:
            #     dic["sale_price"]=""
            # try:
            #     dic["market_price"]=div.xpath('.//div[@class="c-goods-item__market-price  J-goods-item__market-price"]//text()')[1]
            # except:
            #     dic["market_price"]=""
            # try:
            #     dic["discount"]=div.xpath('.//div[@class="c-goods-item__discount  J-goods-item__discount"]/text()')[0]
            # except:
            #     dic["discount"]=""
            # try:
            #     dic["img_link"]="http:"+div.xpath('.//img[@class="J-goods-item__img"]/@src')[0]
            # except:
            #     dic["img_link"]=""
            # try:
            #     dic["details_link"]="https:"+div.xpath('.//a[@target="_blank"]/@href')[0].split('/')[-1].split('.')[0].split('-')[-1]
            # except:
            #     dic["details_link"]=""
            pro_list.append(div.xpath('.//a[@target="_blank"]/@href')[0].split('/')[-1].split('.')[0].split('-')[-1])

            # with open(".//vip.csv", "a", encoding="utf-8") as f:
            #     writer = csv.DictWriter(f, dic.keys())
            #     writer.writerow(dic)
        proIds = ','.join(pro_list)
        print("收集了" + str(len(pro_list)) + "个商品ID")
        # with open(".//vip.csv", "a", encoding="utf-8") as f:
        #     f.write(proIds)
        return pro_list
