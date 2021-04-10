import os
from vip_spider import vip_spider

if __name__ == '__main__':
    keyword = input("请输入采集关键字：")
    path = input("请输入结果保存路径:")
    path += "//%s" % keyword
    try:
        os.mkdir(path)
    except:
        pass
    spider = vip_spider(keyword, path)
    prod_ids = spider.start()
