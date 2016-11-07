# -*- coding: utf-8 -*-
import scrapy
from cityname.items import CitynameItem

class AirbnbSiteSpider(scrapy.Spider):
    name = "airbnb_site"
    allowed_domains = ["insideairbnb.com"]
    start_urls = ['http://insideairbnb.com/get-the-data.html']

    def parse(self, response):
        item = CitynameItem()
        cities_detail = response.xpath('//div[@class="contentContainer"]')

        for city in cities_detail:
            full_name_city = city.xpath('h2/text()').extract()
            table_info = city.xpath('table/tbody/tr')
            for name in full_name_city:
                item['full_name_city'] = name
                yield item
            # for i in table_info:
            #     print(i.xpath('td/text()').extract())
            #     print(i.xpath('td/a/text()').extract())
