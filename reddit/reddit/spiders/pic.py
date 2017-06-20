# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from reddit.items import PicItem

class PicSpider(CrawlSpider):
    name = 'pic'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://reddit.com/r/pics/']

    rules = [
        Rule(LinkExtractor(allow=['/r/pics/\?count=\d*&after=\w*']),
        callback='parse_item',
        follow=True)
    ]

    def parse_item(self, response):
        #print (response.css('h1').extract())

        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = PicItem()
            item['title'] = selector.xpath('div/p/a/text()').extract()
            item['url'] = selector.xpath('a/@href').extract()

            yield item
