# -*- coding: utf-8 -*-
import scrapy
from daili.items import DailiItem

class XidailiSpider(scrapy.Spider):
    name = 'xidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/wt/']

    def parse(self, response):
        print(response.text)
        tbody = response.xpath('//table[@id="ip_list"]/tr')
        #print("tbody",len(tbody))
        for tr in tbody:
            name = DailiItem()
            th = tr.xpath("./td[2]/text()").extract()
            if th:
                #print("tr",type(th),len(th),th[0])
                url = th[0]
            port_ = tr.xpath('./td[3]/text()').extract()
            if port:
                port = port_[0]
            name['name'] = url+":"+port
            yield name
           #ip = tr.xpath('./th[2]/text()').extract()
            #print("ip",ip)




