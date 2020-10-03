# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ECommerceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    img = scrapy.Field()
    cmts = scrapy.Field()

    # def __init__ (self, _url, _title, _rating, _img, _cmts):
    #     self.url = _url
    #     self.title = _title
    #     self.rating = _rating
    #     self.img = _img
    #     self.cmts = cmts
