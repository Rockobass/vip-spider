import json
import requests
import time
from urllib.parse import urlencode, urlparse, quote


#
#
class spuId_spider:
    def __init__(self, prod_ids, keyword):
        self.keyword = keyword
        t = int(round(time.time() * 1000))
        extParams = r'{"stdSizeVids":"","preheatTipsVer":"3","couponVer":"v2","exclusivePrice":"1","iconSpec":"2x",' \
                    r'"ic2label":1} '

        self.params = {
            "app_name": "shop_pc",
            "app_version": "4.0",
            "warehouse": "VIP_SH",
            "fdc_area_id": "103103101",
            "client": "pc",
            "mobile_platform": "1",
            "province_id": "103103",
            "api_key": "70f71280d5d547b2a7bb370a529aeea1",
            "user_id": "",
            "mars_cid": "1609069040453_70d9e4d006cd6d44afc1799df603bafb",
            "wap_consumer": "a",
            "productIds": prod_ids,
            "scene": "search",
            "standby_id": "nature",
            "extParams": extParams,
            "context": "",
            "_": t
        }
        self.url = "https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?" + urlencode(self.params)
        print(self.url)
        self.headers = {
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            "cookie": 'vip_address=%7B%22pid%22%3A%22101103%22%2C%22cid%22%3A%22101103105%22%2C%22pname%22%3A%22'
                      '%5Cu6cb3%5Cu5317%5Cu7701%22%2C%22cname%22%3A%22%5Cu90a2%5Cu53f0%5Cu5e02%22%7D; '
                      'vip_province=101103;vip_city_code=101103105; vip_wh=VIP_BJ; vip_ipver=31; VIP_QR_FIRST=1; '
                      'mars_pid=0; VipUINFO=luc:a|suc:a|bct:c_new|hct:c_new|bdts:0|bcts:0|kfts:0|c10:0|rcabt:0|p2:0|p3'
                      ':1|p4:0|p5:0|ul:3105; user_class=a; mars_sid=5528875c0fcb6ced432cbf6453620746; '
                      'PHPSESSID=9a9efg11n3nah9ua0jjtt0gr13; vip_tracker_source_from=; '
                      'visit_id=79608CF64D5AB73A0AF5DBC01F4EE468; vip_access_times={"list":6,"detail":4}; '
                      'pg_session_no=17; mars_cid=1616550262960_63ea57943137d7888115c8b5935ca173',
            'referer': 'https://category.vip.com/'
        }

        self.payload = {
            "session_id": "-99",
            "mars_cid": "1617946766738_ffa08d5d680ab9d259084a343f852d2e",
            "user_id": "",
            "app_name": "pc",
            "app_type": "web",
            "app_platform": "pc",
            # "monitor_name": "m_performance",
            # "monitor_data": {
            #     "ps_nav": 1569,
            #     "ps_ule": 10,
            #     "ps_rd": 0,
            #     "ps_dlu": 1,
            #     "ps_con": 69,
            #     "ps_req": 432,
            #     "ps_resp": 3,
            #     "ps_dl": 395,
            #     "ps_di": 16,
            #     "ps_dcl": 16,
            #     "ps_dc": 1022,
            #     "ps_le": 9,
            #     "ps_ft": 511,
            #     "ps_ty": 1,
            #     "ps_ttfb": 510,
            #     "ps_ac": 6,
            #     "entriesTotal": 79,
            #     "initiatorType": {
            #         "navigation": {
            #             "n": 1,
            #             "t": 1570
            #         },
            #         "link": {
            #             "n": 5,
            #             "t": 49
            #         },
            #         "script": {
            #             "n": 22,
            #             "t": 1570
            #         },
            #         "img": {
            #             "n": 19,
            #             "t": 0
            #         },
            #         "css": {
            #             "n": 10,
            #             "t": 0
            #         },
            #         "xmlhttprequest": {
            #             "n": 18,
            #             "t": 1178
            #         },
            #         "other": {
            #             "n": 1,
            #             "t": 43
            #         },
            #         "beacon": {
            #             "n": 1,
            #             "t": 91
            #         }
            #     },
            #     "isInit": 0,
            #     "domain": "category.vip.com",
            #     "page_url": "https://category.vip.com/suggest.php?keyword=%s&ff=235|12|1|1" % quote(self.keyword),
            #     "page_name": "category.vip.com/suggest.php",
            #     "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
            # },
            # "monitor_ext": "-99",
            # "monitor_time": 1617946839,
            "app_version": "-99",
            "network": "-99",
            "latitude": "-99",
            "longitude": "-99",
            "model": "-99",
            "os_version": "Windows_10",
            "rom": "-99"
        }

    def getIds(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        dic = json.loads(response.text)
        print(dic)
        spuIds = []
        for p in dic['data']['products']:
            spuIds.append(p['spuId'])
        with open("test.json", 'w') as f:
            for id in spuIds:
                f.write(id + "\n")
            f.close()
        return spuIds
# str = "6917935099234047003,6919240801880875355,6918789300185742299,6917935115154052123,6917935108871869467," \
#       "6917935108871939099,6917935114746041371,6917935115153962011,6917935115170894875,6917998159321757467," \
#       "6918486362038663195,6917935108871775259,6917935100551812123,6917935100534989851,6917935114762843163," \
#       "6918690722615318555,6918789300185734107,6918789300185725915,6919067756724460571,6918783775793677467," \
#       "6918783612697556123,6919067756724452379,6918970508310988699,6919127067575051547,6918802823287335579," \
#       "6918810165190772251,6918560530747376475,6919127067575059739,6918560530747368283,6918753178167854619," \
#       "6918560530747335515,6918560530747360091 "
# sp = SpuIds(prod_ids=str, keyword="春雨")
# sp.getIds()


# url = "https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2?callback=getMerchandiseDroplets1" \
#       "&app_name=shop_pc&app_version=4.0&warehouse=VIP_SH&fdc_area_id=103103101&client=pc&mobile_platform=1" \
#       "&province_id=103103&api_key=70f71280d5d547b2a7bb370a529aeea1&user_id=&mars_cid" \
#       "=1609069040453_70d9e4d006cd6d44afc1799df603bafb&wap_consumer=a&productIds=6917921709890839186" \
#       "%2C6918047293093975826%2C6919240198020474124%2C6917911525058688140%2C6918212477368459781%2C6919240198020457740" \
#       "%2C6917921709033894546%2C6917911526384018508%2C6919247702672714188%2C6919157543465310149%2C6919247702554708428" \
#       "%2C6918892801274130777%2C6919240198071465228%2C6917922360098972882%2C6919249192244007570%2C6919240198054384908" \
#       "%2C6919247702622190028%2C6917911539739755404%2C6919240198088287500%2C6919157543465277381%2C6918892801577763161" \
#       "%2C6919249091657369503%2C6919053236095330949%2C6918751972286447839%2C6919249192244032146%2C6919240198155932940" \
#       "%2C6917921710650008722%2C6919247878716257882%2C6919240198037374220%2C6919244727927928082%2C6919076727247550341" \
#       "%2C6917922360057267282%2C6919240198071481612%2C6919247878766958170%2C6919157543515862981%2C6919240198020506892" \
#       "%2C6919157543380985797%2C6918148587337556997%2C6919240198071313676%2C6919249091825854367%2C6919159174190148549" \
#       "%2C6918686625614599109%2C6919240198071330060%2C6917911526816788620%2C6919249091691124639%2C6919240198037406988" \
#       "%2C6917911526513906380%2C6917922357100168274%2C6919240198155924748%2C6919115586983532172%2C&scene=search" \
#       "&standby_id=nature&extParams=%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22" \
#       "%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%2C%22ic2label%22%3A1%7D&context=&_" \
#       "="
# url = url + t

# dic = {
#     "app_name": "shop_pc",
#     "app_version": "4.0",
#     "warehouse": "VIP_SH",
#     "fdc_area_id": "103103101",
#     "client": "pc",
#     "mobile_platform": "1",
#     "province_id": "103103",
#     "api_key": "70f71280d5d547b2a7bb370a529aeea1",
#     "user_id": "",
#     "mars_cid": "1609069040453_70d9e4d006cd6d44afc1799df603bafb",
#     "wap_consumer": "a",
#     "productIds": "6917921709890839186%2C6918047293093975826%2C6919240198020474124%2C6917911525058688140%2C6918212477368459781%2C6919240198020457740%2C6917921709033894546%2C6917911526384018508%2C6919247702672714188%2C6919157543465310149%2C6919247702554708428%2C6918892801274130777%2C6919240198071465228%2C6917922360098972882%2C6919249192244007570%2C6919240198054384908%2C6919247702622190028%2C6917911539739755404%2C6919240198088287500%2C6919157543465277381%2C6918892801577763161%2C6919249091657369503%2C6919053236095330949%2C6918751972286447839%2C6919249192244032146%2C6919240198155932940%2C6917921710650008722%2C6919247878716257882%2C6919240198037374220%2C6919244727927928082%2C6919076727247550341%2C6917922360057267282%2C6919240198071481612%2C6919247878766958170%2C6919157543515862981%2C6919240198020506892%2C6919157543380985797%2C6918148587337556997%2C6919240198071313676%2C6919249091825854367%2C6919159174190148549%2C6918686625614599109%2C6919240198071330060%2C6917911526816788620%2C6919249091691124639%2C6919240198037406988%2C6917911526513906380%2C6917922357100168274%2C6919240198155924748%2C6919115586983532172%2C",
#     "scene": "search",
#     "standby_id": "nature",
#     "extParams": "%7B%22stdSizeVids%22%3A%22%22%2C%22preheatTipsVer%22%3A%223%22%2C%22couponVer%22%3A%22v2%22%2C%22exclusivePrice%22%3A%221%22%2C%22iconSpec%22%3A%222x%22%2C%22ic2label%22%3A1%7D",
#     "context": "",
#     "_": t
# }

# payload = {
#     "session_id": "-99",
#     "mars_cid": "1617946766738_ffa08d5d680ab9d259084a343f852d2e",
#     "user_id": "",
#     "app_name": "pc",
#     "app_type": "web",
#     "app_platform": "pc",
#     "monitor_name": "m_performance",
#     "monitor_data": {
#         "ps_nav": 1569,
#         "ps_ule": 10,
#         "ps_rd": 0,
#         "ps_dlu": 1,
#         "ps_con": 69,
#         "ps_req": 432,
#         "ps_resp": 3,
#         "ps_dl": 395,
#         "ps_di": 16,
#         "ps_dcl": 16,
#         "ps_dc": 1022,
#         "ps_le": 9,
#         "ps_ft": 511,
#         "ps_ty": 1,
#         "ps_ttfb": 510,
#         "ps_ac": 6,
#         "entriesTotal": 79,
#         "initiatorType": {
#             "navigation": {
#                 "n": 1,
#                 "t": 1570
#             },
#             "link": {
#                 "n": 5,
#                 "t": 49
#             },
#             "script": {
#                 "n": 22,
#                 "t": 1570
#             },
#             "img": {
#                 "n": 19,
#                 "t": 0
#             },
#             "css": {
#                 "n": 10,
#                 "t": 0
#             },
#             "xmlhttprequest": {
#                 "n": 18,
#                 "t": 1178
#             },
#             "other": {
#                 "n": 1,
#                 "t": 43
#             },
#             "beacon": {
#                 "n": 1,
#                 "t": 91
#             }
#         },
#         "isInit": 0,
#         "domain": "category.vip.com",
#         "page_url": "https://category.vip.com/suggest.php?keyword=%E5%8C%A1%E5%A8%81&ff=235|12|1|1",
#         "page_name": "category.vip.com/suggest.php",
#         "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
#     },
#     "monitor_ext": "-99",
#     "monitor_time": 1617946839,
#     "app_version": "-99",
#     "network": "-99",
#     "latitude": "-99",
#     "longitude": "-99",
#     "model": "-99",
#     "os_version": "Windows_10",
#     "rom": "-99"
# }

# payload = "{\"session_id\":\"-99\",\"mars_cid\":\"1617946766738_ffa08d5d680ab9d259084a343f852d2e\",\"user_id\":\"\"," \
#           "\"app_name\":\"pc\",\"app_type\":\"web\",\"app_platform\":\"pc\",\"monitor_name\":\"m_performance\"," \
#           "\"monitor_data\":{\"ps_nav\":1569,\"ps_ule\":10,\"ps_rd\":0,\"ps_dlu\":1,\"ps_con\":69,\"ps_req\":432," \
#           "\"ps_resp\":3,\"ps_dl\":395,\"ps_di\":16,\"ps_dcl\":16,\"ps_dc\":1022,\"ps_le\":9,\"ps_ft\":511," \
#           "\"ps_ty\":1,\"ps_ttfb\":510,\"ps_ac\":6,\"entriesTotal\":79,\"initiatorType\":{\"navigation\":{\"n\":1," \
#           "\"t\":1570},\"link\":{\"n\":5,\"t\":49},\"script\":{\"n\":22,\"t\":1570},\"img\":{\"n\":19,\"t\":0}," \
#           "\"css\":{\"n\":10,\"t\":0},\"xmlhttprequest\":{\"n\":18,\"t\":1178},\"other\":{\"n\":1,\"t\":43}," \
#           "\"beacon\":{\"n\":1,\"t\":91}},\"isInit\":0,\"domain\":\"category.vip.com\"," \
#           "\"page_url\":\"https://category.vip.com/suggest.php?keyword=%E5%8C%A1%E5%A8%81&ff=235|12|1|1\"," \
#           "\"page_name\":\"category.vip.com/suggest.php\",\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
#           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36\"},\"monitor_ext\":\"-99\"," \
#           "\"monitor_time\":1617946839,\"app_version\":\"-99\",\"network\":\"-99\",\"latitude\":\"-99\"," \
#           "\"longitude\":\"-99\",\"model\":\"-99\",\"os_version\":\"Windows_10\",\"rom\":\"-99\"} "

# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
