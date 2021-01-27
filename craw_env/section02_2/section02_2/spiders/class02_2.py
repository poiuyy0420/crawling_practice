import scrapy


class Class022Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Request
        """

        for url in response.css('div.post-item > div > a::attr("href")').getall():
            # url 바로 사용 보다 urljoin 사용
            print(url)
            yield scrapy.Request(response.urljoin(url), self.parse_title)


    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param : response
        :return : Text
        """

        contents = response.css('div.post-body > span > p::text').extract()[:5]

        # contents = response.css('div.post-body > span > p::text').getall()[:5]
        # print(contents)
        # yield {'contents' : contents}
        yield {'contents' : ''.join(contents)}
        # pass



