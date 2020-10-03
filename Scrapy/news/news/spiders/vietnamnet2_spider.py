import scrapy
import json

class VietnamnetSpider(scrapy.Spider):
    name = 'vietnamnet2'
    start_urls = [
        'https://vietnamnet.vn/',
    ]

    def parse(self, response):
        self.write_on_file(response)
        yield from response.follow_all(self.get_next_urls(response), callback=self.parse)

    def write_on_file(self, response):
        with open('/home/straw/Data_mining/Technical_Tutorial/Scrapy/news/vietnamnet2.csv', 'a') as file:
            if len(response.url) >= 70:
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
        potential_urls = response.css('a::attr(href)').getall()
        return self.discard_raw_urls(potential_urls)


    def discard_raw_urls(self, potential_urls):
        next_urls = []

        for url in potential_urls:
            if self.is_raw_url(url) == False:
                next_urls.append(url)

        return next_urls


    def is_raw_url(self, url):
        return 'https' in url or '/vn/' not in url 

