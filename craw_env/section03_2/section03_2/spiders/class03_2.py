import scrapy
import logging

# logger = logger.getLogger('Mylogger')

# 스파이더 종류  : CrawlSpider, XMLFeedSpider, CVSFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com','naver.com', 'daum.net']

    # 실행 방법 1
    # 멀티 도메인
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'http://daum.net']

    # 사용자 시스템 설정(settings.py)
    # custom_settings = {
    #     'DOWNLOAD_DELAY' : 2,
    #     'COOKIES_ENABLED' : True
    # }

    def parse(self, response):
        # logger.info('Response URL1 : %s' % response.url)
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response Status : %s' % response.status)

        if response.url.find('scrapinghub'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }




    # 실행 방법2
    # Request 각각 지정
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse1)
    #     yield scrapy.Request('https://naver.com', self.parse2)
    #     yield scrapy.Request('http://daum.net', , self.parse3)

    # def parse1(self, response):
    #     pass

    # def parse2(self, response):
    #     pass

    # def parse3(self, response):
    #     pass


