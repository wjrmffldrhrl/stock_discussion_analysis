import requests


class StockDiscussionCrawler(object):

    def __init__(self, item_code):
        self.__item_code = item_code
        self.__main_page_url = "/item/board.nhn?"
        self.__base_url = "https://finance.naver.com"
        self.__headers = {
            "referer": self.__base_url + self.__main_page_url + "code=" + item_code,
            "accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed-exchange;v = b3;q = 0.9",
            "accept-encoding": "gzip, deflate, br",
            "cookie": "NNB=VT57OBFJQVKV6; NDARK=N; NRTK=ag#all_gr#0_ma#-2_si#-2_en#-2_sp#-2; ASID=7b8f58320000017607d7445000000061; nx_ssl=2; summary_item_type=recent; _ga=GA1.1.1274548644.1605053669; _ga_7VKFYR6RV1=GS1.1.1611535844.6.1.1611536967.60; nid_inf=758128416; NID_AUT=GmNRL2PHmVyHQpZPmiPQBWPTDlSXvaCXCIEXd2aacnyM7s2H6bq6oT9tDg+hLbgN; NID_JKL=JJhxjjwOqHoasi7A1qm9WC3pz3qtYnTcuT58CGhca34=; BMR=s=1612067442295&r=https%3A%2F%2Fpost.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D30435001%26memberNo%3D1676241%26vType%3DVERTICAL&r2=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fsm%3Dtab_hty.top%26where%3Dnexearch%26query%3D%25EC%2597%2585%25EB%25B9%2584%25ED%258A%25B8%26oquery%3D%25EB%25AC%25B8%25EC%2584%25B8%25EC%259C%25A4%2B1%25EB%25B0%25952%25EC%259D%25BC%2B%25EB%25B6%2588%25EC%25B0%25B8%26tqi%3DhthysdprvOsssSV78%252Bwssssssds-492416; page_uid=hti5qsp0JXosshf3D8lssssstss-180343; naver_stock_codeList=068270%7C005930%7C071840%7C; NID_SES=AAABb1/cL8bEWSN5DZ+BgXtBz3O0FksXbUO6opHIjxGIYqtHNQ7nEQIXcgXEoCwJc87zv+mPfNZhJxVyKaietbCQn1EbI2A60Y44/lBdsvkOxTQnkDWWvOW6Yh6Z0jnJKT9nggYKqHyvgFW8+WfH73Glu7ODteB+ZJR8fl7vtkr88Te4TVWtvAAhvkr2gQUlpMk63annygrfmUwIqY7AvLnFX9xoTorDnCsCA/ES80uhbjicgIOFVEW2KfbUm7Xa3I0aKfRk0hbWP/2QA5q5WjjSliiHiITtKYlIxqf/5k8s7p6tS8LUQzzMUXwVTRvJJ+/8HkdgO8XJg+GLzqkWbFU9t8lyFYf1+viMnYSocZ0YY1+y5mUiVSVwd5OJcYRUgzKXXVDA0p23CjGzJ3zkxe/umlABM7/2TNsCq7nDSr0BQyK/lgHl32PHayVlQD73V5pITzSTSBCa1H2qkhwsfYlGte0jgL6nSVvp8yji7PEx5v0L; CSRF_TOKEN=2fc356f8-6546-4004-a503-1b738526c869; recent_board_read=161658324; JSESSIONID=41C34220DDE75B04857153E247EC78E2",
            "accept-language": "ko-KR, ko;q = 0.9, en-US;q = 0.8, en;q = 0.7",
            "cache-control": "max-age = 0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
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
    print(cr.get("/item/board_read.nhn?code=005930&nid=161662569&st=&sw=&page=1"))
