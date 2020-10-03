import scrapy 

# inherit 
class QuoteSpider(scrapy.Spider):
    # phải đặt tên là name và start_url 
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # parse: phân tích cú pháp 
    def parse(self, response):
        # response is the whole source code, we look for <title> in src and then extract it 
        # add ::text to discard <title></title>
        title = response.css('title::text').extract()[0] 
        # kq trả về sẽ là list, dùng extract_first() để trả về none nếu ko extract đc gì

        author = response.css('small.author::text').extract()

        # The yield statement suspends function’s execution and sends a value back to the caller,
        # but retains enough state to enable function to resume where it is left off. 
        # When resumed, the function continues execution immediately after the last yield run. 
        yield {'title': title}
        yield {'author': author}