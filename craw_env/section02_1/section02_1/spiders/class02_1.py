import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Title Text

        """

        # 2가지(CSS Selector, Xpath)
        #  getall() <-> get() , extract() <-> extract_first()

        # 출력 옵션
        # -o 파일명.확장자 , -t 파일 타입 ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')

        # CSS Selector
        # for text in response.css('div.post-header h2 a::text').getall():
        #     # return Type : Request, BaseItem, Dictionary, None
        #     yield {
        #         'title': text
        #     } 

        # Xpath
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            yield {
                'number': i,
                'text' : text
            }



