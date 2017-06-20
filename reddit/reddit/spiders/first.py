# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        pass
