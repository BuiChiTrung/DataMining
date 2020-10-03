import scrapy
from ..items import ECommerceItem

OUTPUT_FILE = '/home/straw/Data_mining/Scrapy/e_commerce/amazon.csv'

class Amazon(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?k=technology&ref=nb_sb_noss',
    ]
    crawled_links = set({})
    product_cnt = 0

    def parse(self, response):
        if (self.is_product_page(response) == True):
            self.write_item_on_file(response)
        
        yield from response.follow_all(self.get_next_links(response), callback=self.parse)

    def is_product_page(self, response):
        if response.css('meta[name = "title"]') != []:
            return True
        return False


    def write_item_on_file(self, response):
        new_item = self.get_item(response)
        
        if new_item != None:
            self.product_cnt += 1

            with open(OUTPUT_FILE, 'a') as file:
                file.write(f"#===Product {self.product_cnt}:===#\n")
                if (new_item['url'] != None): file.write('Url: ' + new_item['url'] + '\n')
                if (new_item['title'] != None): file.write('Title: ' + new_item['title'].strip('\n') + '\n')
                if (new_item['rating'] != None): file.write('Rating: ' + new_item['rating'] + '\n')
                if (new_item['img'] != None): file.write('Img_url: ' + new_item['img'] + '\n')
                if (new_item['cmts'] != None): file.write('Comments: ' + '\n')

                for cmt in new_item['cmts']:
                    cmt = cmt.strip('\n')
                    file.write(cmt + '\n')


    def get_item(self, response):
        url = response.css("link[rel='canonical']::attr(href)").get()
        if url in self.crawled_links:
            return None

        self.crawled_links.add(url)
        title = response.css("#productTitle::text").get() 
        rating = response.css("span[data-hook='rating-out-of-text']::text").get()  
        img = response.css("img#imgBlkFront::attr(src), #imgTagWrapperId img::attr(src)").get()
        cmts = response.css(".a-expander-partial-collapse-content span::text").getall()
        
        return ECommerceItem(url = url, title = title, rating = rating, img = img, cmts = cmts)

    def get_next_links(self, response):
        return response.css('.a-link-normal.a-text-normal::attr(href), .a-last a::attr(href)').getall()
       
            