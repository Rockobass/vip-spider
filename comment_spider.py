import csv
import requests
import time


class comment_spider:
    def __init__(self, spuId, path):
        self.spuId = spuId
        self.path = path

    def main(self):
        for i in range(1, 10000):
            params = {
                "api_key": "70f71280d5d547b2a7bb370a529aeea1",
                "spuId": self.spuId,
                "page": i,
                "pageSize": 10
            }
            print('第'+str(i)+"页评论")
            flag = self.Get_Comment_Data(params)
            if not flag:
                break

    def Get_Comment_Data(self, params):
        time.sleep(0.5)
        head = {
            "referer": "https://detail.vip.com/",
            "cookie": 'vip_address=%7B%22pid%22%3A%22101103%22%2C%22cid%22%3A%22101103105%22%2C%22pname%22%3A%22'
                      '%5Cu6cb3%5Cu5317%5Cu7701%22%2C%22cname%22%3A%22%5Cu90a2%5Cu53f0%5Cu5e02%22%7D; '
                      'vip_province=101103;vip_city_code=101103105; vip_wh=VIP_BJ; vip_ipver=31; VIP_QR_FIRST=1; '
                      'mars_pid=0; VipUINFO=luc:a|suc:a|bct:c_new|hct:c_new|bdts:0|bcts:0|kfts:0|c10:0|rcabt:0|p2:0|p3'
                      ':1|p4:0|p5:0|ul:3105; user_class=a; mars_sid=5528875c0fcb6ced432cbf6453620746; '
                      'PHPSESSID=9a9efg11n3nah9ua0jjtt0gr13; vip_tracker_source_from=; '
                      'visit_id=79608CF64D5AB73A0AF5DBC01F4EE468; vip_access_times={"list":6,"detail":4}; '
                      'pg_session_no=17; mars_cid=1616550262960_63ea57943137d7888115c8b5935ca173',
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        url = "https://mapi.vip.com/vips-mobile/rest/content/reputation/queryBySpuId_for_pc?"

        text = requests.get(url=url, headers=head, params=params).json()

        if not text.keys().__contains__('data'):
            print(text)
            return False

        if len(text["data"]) < 1:
            return False

        with open("%s//%s_comment.csv" % (self.path, self.spuId), "a+", encoding="utf-8") as f:
            for da in text["data"]:
                dic = {}
                try:
                    dic["authorName"] = da["reputationUser"]["authorName"]
                except:
                    dic["authorName"] = ""
                try:
                    dic["vips"] = da["reputationUser"]["vips"]
                except:
                    dic["vips"] = ""
                try:
                    dic["brandName"] = da["reputationProduct"]["brandName"]
                except:
                    dic["brandName"] = ""
                # try:
                #     dic["discountTips"] = da["reputationProduct"]["discountTips"]
                # except:
                #     dic["discountTips"] = ""
                try:
                    dic["goodsName"] = da["reputationProduct"]["goodsName"]
                except:
                    dic["goodsName"] = ""
                # try:
                #     dic["vipShopPrice"] = da["reputationProduct"]["vipShopPrice"]
                # except:
                #     dic["vipShopPrice"] = ""
                try:
                    dic["content"] = da["reputation"]["content"]
                except:
                    dic["content"] = ""
                # try:
                #     dic["impresses"] = da["reputation"]["impresses"]
                # except:
                #     dic["impresses"] = ""
                # try:
                #     dic["usefulCount"] = da["reputation"]["usefulCount"]
                # except:
                #     dic["usefulCount"] = ""
                # try:
                #     dic["postTime"] = da["reputation"]["postTime"]
                # except:
                #     dic["postTime"] = ""

                writer = csv.DictWriter(f, dic.keys())
                writer.writerow(dic)
        return True

