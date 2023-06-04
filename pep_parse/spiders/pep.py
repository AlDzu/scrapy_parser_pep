# scrapy crawl pep
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        tbody = response.css('tbody')
        pep_hrefs = tbody.css('a::attr(href)')
        for pep in pep_hrefs:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        head = response.css("h1.page-title::text").get().strip().split(" – ")
        # обратно не понял. в константы можно вынести разве что номер
        # с прицелом ссылки из него собирать? их получаем немного выше.
        # ['PEP 1', 'PEP Purpose and Guidelines']
        number = (head[0])
        name = (head[-1])
        if name is None:
            name = ' '
        status = response.css('dt:contains("Status") + dd > abbr::text').get()
        pep_info = {
            "number": number.split(" ")[-1],
            "name": name,
            "status": status,
        }
        yield PepParseItem(pep_info)
