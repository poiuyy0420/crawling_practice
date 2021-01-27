import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItem


class NewsSpider(CrawlSpider):
    name = 'test12'
    allowed_domains = ['news.daum.net', 'v.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(장규표현식 사용 추천)
    # page=\d$ : 1자리 수
    # page=\d+ : 연속, follow=True
    rules = [
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)
        
        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # URL 신문 기사 URL
            article_url = url.css('strong > a::attr(href)').extract_first().strip()
            # self.logger.info('--------------------->', article_url)
            # 요청
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url})

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        # self.logger.info('==================================================')
        # self.logger.info('Response From Parent URL : %s' % response.meta['parent_url'])
        # self.logger.info('Child Response UR : %s' % response.url)
        # self.logger.info('Child Response Status : %s' % response.status)
        # self.logger.info('==================================================')

        # 헤드라인
        headline = response.css('h3.tit_view::text').get().strip()

        # 본문
        c_list = response.css('div.article_view p::text').extract()
        contents = ''.join(c_list).strip()

        yield ArticleItem(headline=headline, contents=contents, parent_link=response.meta['parent_url'], article_link=response.url)

