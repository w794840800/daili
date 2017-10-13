# -*- coding: utf-8 -*-
import scrapy


class KuiadailiSpider(scrapy.Spider):
    name = 'kuiadaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://kuaidaili.com/']

    def parse(self, response):
        pass
