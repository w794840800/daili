# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DailiPipeline(object):
    def process_item(self, item, spider):
        if spider.name =='xidaili':
            with open("xidaili.txt","a") as f :
                f.write(item['name']+'\n')

        elif spider.name == 'kuiadaili':
            with open("kuiadaili.txt",'a') as  f:
                f.write(item['name']+'\n')

        return item
