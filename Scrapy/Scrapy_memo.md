# Description

### quotetutorial
1. quotes_spider:
   + spider cơ bản, yield
   + Selector Gadget tool
2. quotes_spider2:
   + sử dụng items.py để tạo item containers từ đó có thể cho vào db
   + cho data vào file 

# Memo

### I. Scrapy: là một package của python dùng để crawl data. Thành phần:
<img src = "https://viblo.asia/uploads/b546496a-8a45-4260-a6d4-9037fc888e7c.png">

1. Scrapy Engine
Scrapy Engine có trách nhiệm kiểm soát luồng dữ liệu giữa tất cả các thành phần của hệ thống và kích hoạt các sự kiện khi một số hành động xảy ra

2. Scheduler
Giống như một hàng đợi (queue), scheduler sắp xếp thứ tự các URL cần download

3. Dowloader
Thực hiện dowload trang web và cung cấp cho engine

4. Spiders
Spiders là class được viết bởi người dùng, chúng có trách nhiệm bóc tách dữ liệu cần thiết và tạo các url mới để nạp lại cho scheduler qua engine.

5. Item Pipeline
Những dữ liệu được bóc tách từ spiders sẽ đưa tới đây, Item pipeline có nhiệm vụ xử lý chúng và lưu vào cơ sở dữ liệu

6. Các Middlewares
Là các thành phần nằm giữa Engine với các thành phần khác, chúng đều có mục địch là giúp người dùng có thể tùy biến, mở rổng khả năng xử lý cho các thành phần. VD: sau khi dowload xong url, bạn muốn tracking, gửi thông tin ngay lúc đó thì bạn có thể viết phần mở rộng và sửa lại cấu hình để sau khi Dowloader tải xong trang thì sẽ thực hiện việc tracking.

   + Spider middlewares
Là thành phần nằm giữa Eninge và Spiders, chúng xử lý các response đầu vào của Spiders và đầu ra (item và các url mới).

   + Dowloader middlewares
Nằm giữa Engine và Dowloader, chúng xử lý các request được đẩy vào từ Engine và các response được tạo ra từ Dowloader

   + Scheduler middlewares
Nằm giữa Engine và Scheduler để xử lý những requests giữa hai thành phần

2. Luồng dữ liệu

### II. Scrapy structure 
    scrapy startproject proj_name 
1. spiders viết ctr python để crawl
2. settings.py
   + CONCURRENT_REQUESTS: số request đồng thời đc gửi đi trong 1s, mặc định 16, nếu cao quá => sập web or bị chặn 
   + ROBOTSTXT_OBEY: (luật crawl: site_name/robots.txt) scrapy sẽ tự tuần theo luất ko crawl mấy cái link trong đó. Muốn crawl thì thay đổi thành False 
3. items.py
    define các field của product. VD: category, price, ...
4. pipelines.py
   define the way we save crawled data. Ex: by json file, mysql,...
5. middlewares.py 
   tùy biến, mở rộng khả năng xử lí các request, response 

### III. Run spider
    scrapy crawl spider_name
1. Dùng yield thay cho return trong các func 

### IV. Xpath: https://www.accordbox.com/blog/scrapy-tutorial-7-how-use-xpath-scrapy/
http://quotes.toscrape.com/

```
#If we want to get html node
response.xpath("/html").extract()

#If we want to get body node, which is the child of html node
response.xpath("/html/body").extract()

#If you want to get all div descendant of this html
response.xpath("/html//div").extract()

#we can also drill down without having to start with /html, this expression would extract all div nodes
response.xpath("//div").extract()

response.xpath("//div[@class='quote']").extract()

# you can use this syntax to filter nodes
response.xpath("//div[@class='quote']/span[@class='text']").extract()

# use text() to extract all text inside nodes
response.xpath("//div[@class='quote']/span[@class='text']/text()").extract()

# combine css + xpath to get attribute
response.css("li.next a").xpath("@href").extract()
```

### V. CSS selector 
1. * : all elem
2. tag_name[attr]: vd a[href] lấy tất cả tag a có attr href
   tag_name[attr="x"]: get all tag_name with attr = "x"
   tag_name[attr^="x"]: attr mở đầu = "x"
   tag_name[attr$="x"]: attr kết thúc = "x"
   tag_name[attr*="x"]: attr chứa = "x"
3. tag.class
   tag#id
4. a b: b is descendant of a
5. a>b: b is son of a
6. a+b: b is brother ngay sau a (các brother != của a ko đc pick)
7. a~b: b is brothers sau a  

### VI. Bypass website restriction
1. Use user-agent
   + VD: amazon cho phép google bot crawl dữ liệu thoải mái để nó hiện thì sản phẩm của amazon khi gg search. Nên ta disguise as google bot. Search google user agent
   ```
      USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
   ```
   + However, đến một lúc amazon nó cx phát hiện đc đang fake => rotate các user agent khác nhau bằng package
   scrapy-user-agents
   ```
      DOWNLOADER_MIDDLEWARES = {
      'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
      'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
      }
   ```
2. Use proxies
   + Thay đổi IP address liên tục. Proxie là những cái IP ko phải của mình và cx ko phải của một máy nào khác
   ```
      PROXY_POOL_ENABLED = True

      DOWNLOADER_MIDDLEWARES = {
         # ...
         'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
         'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
         # ...
      }
   ``` 
3. Statistic
   + Chay: 16 products
   + Google bot: 47 products
   + Scrapy-users-agent: +oo 

### Stuff
1. Shell: 
```
scrapy shell web_link
```
2. Ném data crawl đc vào file 
```
scrapy crawl -o file_name.(json/csv/xml)
```
3. Scrapy Request
   + request: chỉ nhận đường link tuyệt đối (phải thêm https://vnexpress)
   ```
   def parse_page1(self, response):
      return scrapy.Request("http://www.example.com/some_page.html",
                           callback=self.parse_page2)

   def parse_page2(self, response):
      # this would log http://www.example.com/some_page.html
      self.logger.info("Visited %s", response.url)
   ```
   + follow: nhận cả link tương đối nhưng phải có response 
   ```
   yield from response.follow_all(list_links, callback = self.parse)
   ```

4. Phần <head> của page cx chứa nhiều thông tin quan trọng mà ta cần quan tâm tới 
5. Phần biết page chưa thông tin cần lấy với page ko bằng cách quan sát src code tìm điểm đb của các page cần lấy data. Dùng trong trường hợp bị bug select đúng nhưng ko trả ra gì (xem thẻ body)
6. Thêm allowed_domains to avoid other domains
   ```
      allowed_domains = ['vnexpress.net']
   ```   
7. DDos: denial of service attack - tấn công từ chối dịch vụ 
   gửi một đống request lên server làm server sập 
8.  Với những trang redirect đổi chữ r thành c
+  Quét bằng mã trang xg lùi dần => siêu nhanh nhưng đối với trang bán hàng chú ý ko bị DDoS
10. Convert dict thành json object 
    ```
      json.dump(data, enforced_ascii=False)
    ```