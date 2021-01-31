import requests


class StockDiscussionCrawler(object):

    def __init__(self, item_code):
        self.__item_code = item_code
        self.__main_page_url = "/item/board.nhn?"
        self.__base_url = "https://finance.naver.com"
        self.__headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "finance.naver.com",
            # "referer": "https://finance.naver.com/item/board.nhn?code=005930&page=40"
        }

    def __get_discussion_script(self, discussion_url):
        target_url = self.__base_url + discussion_url
        request = requests.get(url=target_url, headers=self.__headers)
        return request.text

    def get(self, discussion_url):
        return self.__get_discussion_script(discussion_url)

    # def __save_script(self):


if __name__ == '__main__':
    cr = StockDiscussionCrawler("005930")
    print(cr.get("/item/board_read.nhn?code=005930&nid=161680006&st=&sw=&page=1"))
