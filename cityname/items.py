# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CitynameItem(scrapy.Item):
    # define the fields for your item here like:
    full_name_city = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    dataset = scrapy.Field()
    dataset = scrapy.Field()
    pass
