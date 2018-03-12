# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IvskyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Referer
    referer = scrapy.Field()
    #图片地址
    url = scrapy.Field()
    #图片名字
    name = scrapy.Field()
    #图片分类位置
    pos = scrapy.Field()
    #图片分辨率
    resolution = scrapy.Field()
    pass
