import json 
import scrapy 

OUTPUT_FILE = '/home/straw/Data_mining/Scrapy/e_commerce/tiki.txt'

class Tiki(scrapy.Spider):
    name = 'tiki'


    def start_requests(self):
        start_url = 'https://tiki.vn/?src=header_tiki'
        yield scrapy.Request(start_url, callback = self.parse_categories)


    def parse_categories(self, response):
        categories = response.css("ul.Navigation__Wrapper-knnw0g-0.jJSxyD li a::attr(href)").getall()
        for category in categories:
            yield scrapy.Request(category, callback = self.parse_products)

    
    def parse_products(self, response):
        if response.status == 200:
            products = response.css("div.product-box-list div a::attr(href)").getall()
            for product in products:
                #print(product)
                #if isinstance(product, str):
                yield scrapy.Request("https://tiki.vn" + product, callback = self.parse_product)

            for next_products_page in response.css("div.list-pager ul li a::attr(href)").getall():
                print(next_products_page, "hahahahahaahaaaaaaaaaaaaaaa")
                yield scrapy.Request("https://tiki.vn" + next_products_page, callback = self.parse_products)


    
    def parse_product(self, response):
        if response.status == 200:
            product_data ={
                "product_url" : response.url,
                "image_url" : response.css("div.ImageLens__Wrapper-uaw433-0.jcyqbC div img::attr(src)").getall(),
                "price": response.css("div.price-and-icon p.price::text").get()
            }

            with open(OUTPUT_FILE, 'a') as out_file:
                out_file.write(json.dumps(product_data, ensure_ascii=False))
                out_file.write('\n')

