# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from cityname.items import CitynameItem

class AirbnbSiteSpider(scrapy.Spider):
    name = "airbnb_site"
    allowed_domains = ["insideairbnb.com"]
    start_urls = ['http://insideairbnb.com/get-the-data.html']

    def parse(self, response):
        item = CitynameItem()
        full_name_city = response.xpath('//div[@class="contentContainer"]/h2/text()')
        for city_name in full_name_city:
            item['full_name_city'] = city_name.extract()
            yield item
