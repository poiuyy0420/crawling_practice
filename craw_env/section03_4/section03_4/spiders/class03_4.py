import scrapy
from ..items import ItArticle


class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['computerworld.com']
    start_urls = ['https://computerworld.com/news/']

    # 메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return : Request
        """

        for url in response.css('div.main-col > div.river-well.article > div.post-cont > h3 > a::attr(href)').extract():
            # print("====>", url)
            print("====>", response.urljoin(url))
            yield scrapy.Request(response.urljoin(url), self.parse_news)
            
    
    def parse_news(self, response):
        """
        :param : response
        :return : Items
        """

        item = ItArticle()
        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['img_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] = ''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall())

        # print(dict(item))
        # print(dir(dict(item)))

        yield item

