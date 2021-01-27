# 파이프라인 실습(1)
# 예1) 잘못된 데이터 제거, DB 저장, SNS/SMS/메일 전송 

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class TestPipeline(object):
    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started.')


    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Closed.')

