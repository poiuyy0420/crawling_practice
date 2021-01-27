import scrapy

# scrapy 환경설정
# 중요

# 실행방법
# 1. 커맨드 라인 실행 -> scrapy crawl 크롤러명 -s(--set) <NAME>=<VALUE>
# 2. Spider 실행 시 직접 지정
# 3. Settings.py에 지정 -> 추천
# 4. 서브 명령어 (X)
# 5. 글로버 설정 : scrapy.settings.default_settings

class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):
        # xpath + css 혼합
        for i, v in enumerate(response.xpath('//div[@class="post-summary-content"]').css('div.post-excerpt-container > h3 > a::text').extract(), 1):
            # 인덱스 번호, 헤드라인
            yield dict(num=i, headline=v)