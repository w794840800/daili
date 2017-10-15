# -*- coding: utf-8 -*-
import scrapy

from daili.items import DailiItem
class KuiadailiSpider(scrapy.Spider):
    name = 'kuiadaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/']

    def parse(self, response):
        #print(response.text)
        content = response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
        for tr in content:
            name = DailiItem()
            ip = tr.xpath('./td[1]/text()').extract()[0]
            print('td',ip)
            port = tr.xpath('./td[2]/text()').extract()[0]
            print('port',port)
            name['name'] = ip+":"+port
            yield name