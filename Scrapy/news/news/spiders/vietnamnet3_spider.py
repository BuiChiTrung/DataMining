import scrapy
import json
from queue import Queue

OUTPUT_FILE = '/home/straw/Data_mining/Technical_Tutorial/Scrapy/news/vietnamnet3.csv'

class VietnamnetSpider(scrapy.Spider):
    name = 'vietnamnet3'
    allowed_domains = ['vietnamnet.vn']
    start_urls = [
        
        # 'https://vietnamnet.vn/vn/kinh-doanh/'
        # 'https://vietnamnet.vn/vn/giai-tri/'
        # 'https://vietnamnet.vn/vn/the-gioi/'
        # 'https://vietnamnet.vn/vn/doi-song/'
        'https://vietnamnet.vn/'
        # 'https://vietnamnet.vn/vn/the-thao/'
        
    ]
    hash_table = [0 for i in range(1606084)]
    frontier = Queue(maxsize = 5000)

    def parse(self, response):
        self.write_on_file(response)
        self.get_next_urls(response)
        
        while self.frontier.empty() == False:
            url = self.frontier.get()
            yield scrapy.Request('https://vietnamnet.vn' + url, callback=self.parse)

    def write_on_file(self, response):
        if response.status == 200 and len(response.url) >= 60:
            with open(OUTPUT_FILE, 'a') as file:
                data = {
                    'url':response.url,
                    'title':response.css('title::text').get(),
                    'tag':response.css('.top-cate-head-title a::text').extract(),
                    'date':self.format_date(response.css('.ArticleDate::text').extract()),
                    'summary':response.css('meta[name="description"]::attr(content)').get()
                }
                file.write(json.dumps(data, ensure_ascii=False) + '\n')


    def format_date(self, date):
        if date == []: return []

        date = date[0].split('\n')
        for i in range (len(date)):
            date[i] = date[i].strip(' ')
        date = ' '.join(date)
        return [date]
        

    def get_next_urls(self, response):
        self.discard_in_queue_url(response.css('a[href^="https://vietnamnet.vn"], a[href^="/"]::attr(href)').getall())
        
    def discard_in_queue_url(self, potential_urls):
        for url in potential_urls:
            hash_code = hash(url) % 1606081
            if (self.hash_table[hash_code] == 0):
                #print(url)
                self.hash_table[hash_code] = 1 
                self.frontier.put(url)




