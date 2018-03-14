# !/usr/bin/env pyhton
# -*- coding: utf-8 -*-

"""
本程序是用来爬取豆瓣阅读的所有标签下的内容，采用随机头，随机代理来越过反爬取机制。
"""

from  scrapy import Spider, Request
from ..items import DoubanreadingItem


class ReadingSpider(Spider):
    name = 'reading'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']
    base_url = 'Https://book.douban.com'

    def parse(self, response):
        # 先找出主页面下的所有分类标签。
        tags = response.xpath('//table[@class="tagCol"]/tbody/tr/td/a/@href').extract()
        for tag in tags:
            print('Now crawling tag:%s' % tag)
            # 发起所有的标签请求。
            yield Request(self.base_url + tag, self.parse_group)


    def parse_group(self, response):
        # 书籍信息块。
        books_info = response.xpath('//ul/li/div[@class="info"]')
        if books_info:
            for sigle_book in books_info:
                score = sigle_book.xpath('./div[2]/span[2]/text()').extract_first().replace('\n', '').replace(' ', '')
                voter = sigle_book.xpath('./div[2]/span[3]/text()').extract_first().replace('\n', '').replace(' ', '')
                # print(score, voter)
                # 筛选。
                if eval(voter[1:-4]) >= 2000 and eval(score) >= 8.0:
                    href = sigle_book.xpath('./h2/a/@href').extract_first()
                    print('Is parsing %s' % href)
                    yield Request(href, self.parse_detail)
                    next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
                    if next_page:
                        yield Request(self.base_url + next_page)
                    else:
                        print('This is the last page.')
                else:
                    return None
        else:
            return None

    def parse_detail(self, response):
        item = DoubanreadingItem()
        item['name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        item['author'] = response.xpath('//*[@id="info"]/a[1]/text()').extract_first().replace('\n', '').replace(' ', '')
        item['translator'] = response.xpath('//*[@id="info"]/span/a/text()').extract_first()
        item['voter'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()').extract_first()
        item['rating'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        item['introduction'] = '\n'.join(response.xpath('//*[@id="link-report"]/div[1]/div/p/text()').extract())
        item['author_introduction'] = '\n'.join(response.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/p/text()').extract())
        item['hottest_comment'] = '\n'.join(response.xpath('//*[@id="comments"]/ul/li/div/p/text()').extract())
        yield item
