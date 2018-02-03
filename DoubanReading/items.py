# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class DoubanreadingItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    author = Field()
    translator = Field()
    voter = Field()
    rating = Field()
    introduction = Field()
    author_introduction = Field()
    hottest_comment = Field()

