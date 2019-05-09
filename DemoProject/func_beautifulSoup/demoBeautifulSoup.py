import os
from common.logger import get_logger

logger = get_logger(os.path.splitext(os.path.basename(__file__))[0])


# def demo():
#     logger.info("Demo START")
#
#     import requests
#     from bs4 import BeautifulSoup
#
#     # 下載Yahoo 首頁內容
#     r = requests.get('https://tw.yahoo.com')
#     # 確認是否下載成功
#     if r.status_code == requests.codes.ok:
#         # 以BeautifulSoup 解析HTML 程式碼
#         soup = BeautifulSoup(r.text, ' html.parser ')
#
#         # 以CSS 的class 抓出各類頭條新聞
#         stories = soup.find_all(' a ', class_=' story-title ')
#         for s in stories:
#             # 新聞標題
#             print(" 標題： " + s.text)
#             # 新聞網址
#             print(" 網址： " + s.get(' href '))
#
#     logger.info("Demo END")


def demo():
    logger.info("Demo START")

    import urllib.request
    from bs4 import BeautifulSoup

    quote_page = 'http://10.52.179.4/webOfficial'
    response = urllib.request.Request(quote_page)
    with urllib.request.urlopen(response) as res:
        body = res.read()
        logger.info("\n" + body.decode(encoding='utf-8'))

    soup = BeautifulSoup(body, 'html.parser')
    name_box = soup.find('div', attrs={'class': 'clasTopics'})
    topics = name_box.text.strip()
    logger.info("\n" + topics)

    logger.info("Demo END")

