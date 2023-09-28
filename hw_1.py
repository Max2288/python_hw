import requests

cookies = {
    'ys': 'newsca.native_cache#ybzcc.ru#svt.1#def_bro.0',
    'i': 'pAtddJvpGiumZB3KHMB53Falri3hFb9avVPpMDnG3u1qh0dAyniDPPBNZ/Gx2e44c1khRzqDzoHkLFRWbL2cxf3Ha0U=',
    'yandexuid': '8262564661689323959',
    'is_gdpr': '0',
    'is_gdpr_b': 'CO3+UxDbwgEoAg==',
    'yuidss': '8262564661689323959',
    'ymex': '2004683973.yrts.1689323973',
    'gdpr': '0',
    '_ym_uid': '1689323974668448973',
    'L': 'RAdeQWd/S1tZemJGcVlda0YIRAxvAHZCJEZbOVUoDw==.1689324069.15403.388938.c8f479d9bb3f9cac6e08fe0629b88b5d',
    'yandex_login': 'm.bzbdv',
    'my': 'YwA=',
    'font_loaded': 'YSv1',
    'cycada': 'I2TMF8kSp3rXqCVlypW1BpW/9RX4Gm2mGOHs5Pck9FY=',
    'lastVisitedPage': '%7B%7D',
    'sae': '0:CDA53E75-5185-4F48-AF82-5186A08CCA6F:p:23.7.5.739:w:d:RU:20230714',
    'yp': '1695304784.uc.ru#1695304784.duc.ru#1720860070.brd.6302000000#1720860070.cld.2270452#2004684069.udn.cDptLmJ6YmR2#1710811360.szm.1_25:1536x864:1488x716#2010573709.pcs.1#1695298788.gpauto.43_401321:39_979172:140:1:1695291588#1696168120.hdrc.1',
    'device_id': 'a90ab74d36f674e65d4a18bbaf25713654796b7c9',
    'active-browser-timestamp': '1695292017163',
    '_ym_d': '1695292017',
    'Session_id': '3:1695292018.5.0.1689324069844:ScSuVQ:7b.1.2:1|1793348404.0.2.3:1689324069|3:10276073.320043.5IQY_6lB2EX2y3yn5IqqEJYAEAQ',
    'sessar': '1.1182.CiAtcZUalAUIK2fpvgHSjVitsXB7O3k9fYkQc-YSmqJfIg.Lwoz6ZYAL5HDKHqUol5idd58344SKivP7GfFLKTwbqc',
    'sessionid2': '3:1695292018.5.0.1689324069844:ScSuVQ:7b.1.2:1|1793348404.0.2.3:1689324069|3:10276073.320043.fakesign0000000000000000000',
    '_ym_isad': '1',
    '_ym_visorc': 'b',
    '_yasc': '4CQiPI6T6aPLBOuXDLHDoSpZjV/zeZJbhvutNu1kIFvtcRfk4d43PgJDuHFks6JU3cVdeODq1OqftAK6JA==',
    'bh': 'EjsiTm90LkEvQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjExNCIsICJZYUJyb3dzZXIiO3Y9IjIzIhoFIng4NiIiDCIyMy43LjUuNzM5IioCPzA6CSJXaW5kb3dzIkIIIjE1LjAuMCJKBCI2NCJSUyJOb3QuQS9CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTQuMC41NzM1LjI4OSIsIllhQnJvd3NlciI7dj0iMjMuNy41LjczOSIi',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ys=newsca.native_cache#ybzcc.ru#svt.1#def_bro.0; i=pAtddJvpGiumZB3KHMB53Falri3hFb9avVPpMDnG3u1qh0dAyniDPPBNZ/Gx2e44c1khRzqDzoHkLFRWbL2cxf3Ha0U=; yandexuid=8262564661689323959; is_gdpr=0; is_gdpr_b=CO3+UxDbwgEoAg==; yuidss=8262564661689323959; ymex=2004683973.yrts.1689323973; gdpr=0; _ym_uid=1689323974668448973; L=RAdeQWd/S1tZemJGcVlda0YIRAxvAHZCJEZbOVUoDw==.1689324069.15403.388938.c8f479d9bb3f9cac6e08fe0629b88b5d; yandex_login=m.bzbdv; my=YwA=; font_loaded=YSv1; cycada=I2TMF8kSp3rXqCVlypW1BpW/9RX4Gm2mGOHs5Pck9FY=; lastVisitedPage=%7B%7D; sae=0:CDA53E75-5185-4F48-AF82-5186A08CCA6F:p:23.7.5.739:w:d:RU:20230714; yp=1695304784.uc.ru#1695304784.duc.ru#1720860070.brd.6302000000#1720860070.cld.2270452#2004684069.udn.cDptLmJ6YmR2#1710811360.szm.1_25:1536x864:1488x716#2010573709.pcs.1#1695298788.gpauto.43_401321:39_979172:140:1:1695291588#1696168120.hdrc.1; device_id=a90ab74d36f674e65d4a18bbaf25713654796b7c9; active-browser-timestamp=1695292017163; _ym_d=1695292017; Session_id=3:1695292018.5.0.1689324069844:ScSuVQ:7b.1.2:1|1793348404.0.2.3:1689324069|3:10276073.320043.5IQY_6lB2EX2y3yn5IqqEJYAEAQ; sessar=1.1182.CiAtcZUalAUIK2fpvgHSjVitsXB7O3k9fYkQc-YSmqJfIg.Lwoz6ZYAL5HDKHqUol5idd58344SKivP7GfFLKTwbqc; sessionid2=3:1695292018.5.0.1689324069844:ScSuVQ:7b.1.2:1|1793348404.0.2.3:1689324069|3:10276073.320043.fakesign0000000000000000000; _ym_isad=1; _ym_visorc=b; _yasc=4CQiPI6T6aPLBOuXDLHDoSpZjV/zeZJbhvutNu1kIFvtcRfk4d43PgJDuHFks6JU3cVdeODq1OqftAK6JA==; bh=EjsiTm90LkEvQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjExNCIsICJZYUJyb3dzZXIiO3Y9IjIzIhoFIng4NiIiDCIyMy43LjUuNzM5IioCPzA6CSJXaW5kb3dzIkIIIjE1LjAuMCJKBCI2NCJSUyJOb3QuQS9CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTQuMC41NzM1LjI4OSIsIllhQnJvd3NlciI7dj0iMjMuNy41LjczOSIi',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.739 Yowser/2.5 Safari/537.36',
    'X-Current-UID': '1793348404',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-09-21T13:27:42+03:00',
    'Y-Browser-Experiments': 'NjczMTM3LDAsMzE=',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.8599263673920186',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)