# -*- coding: utf-8 -*-
import scrapy


class XidailiSpider(scrapy.Spider):
    name = 'xidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://xicidaili.com/']

    def parse(self, response):
        pass
