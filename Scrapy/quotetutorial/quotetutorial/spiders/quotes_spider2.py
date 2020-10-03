import scrapy 
from ..items import QuotetutorialItem


# inherit 
class QuoteSpider(scrapy.Spider):
    # phải đặt tên là name và start_url 
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # parse: phân tích cú pháp 
    def parse(self, response):
        # create instance 
        quote_item = QuotetutorialItem()

        # Ko đc extract vì sẽ trả về string => ko .css() đc 
        all_quote_division = response.css("div.quote")

        for quote in all_quote_division:
            title = quote.css("span.text::text").extract()
            author = quote.css("small.author::text").extract()
            tags = quote.css("a.tag::text").extract()

            quote_item['title'] = title
            quote_item['author'] = author 
            quote_item['tags'] = tags

            yield quote_item