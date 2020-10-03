import scrapy
from ..items import NewsItem



class Kenh14Spider(scrapy.Spider):
    name = 'kenh14'
    start_urls = [
        'https://kenh14.vn/them-21-ca-mac-covid-19-moi-trong-do-co-20-ca-lien-quan-den-da-nang-20200808175412698.chn',
        'https://kenh14.vn/tran-thanh-co-kem-duyen-khi-lien-tuc-nhac-ten-tinh-cu-cua-vo-trong-rap-viet-20200809023953464.chn',
        'https://kenh14.vn/ronaldo-viet-tam-thu-gui-toi-fan-ham-mo-sau-ket-qua-dang-that-vong-tai-champions-league-lap-tuc-nhan-ve-hang-trieu-luot-tha-tim-20200809053040152.chn',
        'https://kenh14.vn/blackpink-se-the-nao-khi-cat-toc-con-trai-jisoo-trong-banh-beo-the-ma-ai-ngo-lai-la-trum-cuoi-20200809001111105.chn',
        'https://kenh14.vn/wowy-giai-thich-ly-do-xin-loi-va-tra-lai-chu-heo-dat-cho-thi-sinh-rap-viet-cau-noi-cua-em-lam-anh-chanh-long-20200808224522105.chn',
        'https://kenh14.vn/khoe-khuc-ca-ro-ran-mac-van-khoa-nhan-ngay-bao-likes-khong-chi-boi-ca-ngon-ma-con-co-y-nghia-rat-dac-biet-20200809090101386.chn',
        'https://kenh14.vn/loat-khoanh-khac-cung-muon-xiu-trong-ngay-thi-thpt-quoc-gia-dau-tien-xem-xong-thay-yeu-doi-han-20200809110029683.chn',
        'https://kenh14.vn/mina-aoa-nhap-vien-khan-sau-khi-cat-co-tay-tu-tu-giua-dem-cong-ty-quan-ly-tiet-lo-tinh-trang-hien-tai-2020080910224323.chn',
        'https://kenh14.vn/bi-vong-bo-vui-dap-box-gaming-van-thi-dau-xuat-sac-giu-nguyen-co-hoi-tranh-ngoi-vo-dich-pubg-mobile-the-gioi-2020080902502048.chn',
        'https://kenh14.vn/loat-khoanh-khac-xuat-than-duoc-chup-boi-nhung-tay-may-nghiep-du-la-minh-chung-song-cho-cau-noi-hay-khong-bang-hen-20200804184346633.chn',
        'https://kenh14.vn/chuyen-it-ai-biet-nhieu-nu-idol-han-quoc-la-nhung-con-nghien-game-thu-thiet-20200808085100417.chn',
        'https://kenh14.vn/10-bi-kip-tam-ly-cuc-dinh-giup-ban-tu-tin-giao-tiep-ma-dam-bao-doi-phuong-ai-cung-thich-me-20200802173152305.chn',
        'https://kenh14.vn/cau-chuyen-phia-sau-hinh-anh-nguoi-dan-ong-tong-ngong-duoi-nhau-voi-lon-loi-quanh-cong-vien-20200808131218042.chn',
        'https://kenh14.vn/tung-bi-cho-duoi-can-den-am-anh-nam-sinh-che-tao-thiet-bi-duoi-cho-cuc-ky-hieu-qua-20200106151605754.chn',
        'https://kenh14.vn/chang-trai-viet-dau-tien-duoc-lam-viec-cung-nha-soan-nhac-huyen-thoai-cua-lion-king-the-dark-knight-inception-20200721112043559.chn',
        'https://kenh14.vn/samsung-galaxy-note20-khac-gi-galaxy-note10-20200806052451836.chn',
        'https://kenh14.vn/doanh-thu-phong-ve-trung-sut-giam-lan-dau-tien-trong-8-nam-co-endgame-do-van-khong-keo-noi-khan-gia-ra-rap-20190709141757022.chn',
        'https://kenh14.vn/so-bi-can-roy-jones-tinh-mua-bao-hiem-tai-truoc-tran-dai-chien-voi-mike-tyson-20200807101915848.chn'
        # 'https://kenh14.vn/nhom-chu-de/doc-cham.chn' 
    ]
    
    #links_set = {'https://kenh14.vn/them-21-ca-mac-covid-19-moi-trong-do-co-20-ca-lien-quan-den-da-nang-20200808175412698.chn'}
    #links_set = {}
    links_set = set(start_urls)
        
    def parse(self, response):
        # get new article
        kenh14_item = NewsItem()

        kenh14_item['title'] = response.css(".kbwc-title::text").extract()
        kenh14_item['author'] = response.css(".kbwcm-author::text").extract()
        kenh14_item['date'] = response.css(".kbwcm-time::text").extract()
        kenh14_item['tag'] = response.css(".kli a::text").extract()

        if kenh14_item['title'] != []:
            #write on new article on file
            file = open('/home/straw/Data_mining/Scrapy/news/kenh14.txt', 'a')

            file.write('Title: '  + kenh14_item['title'][0] + '\n')
            file.write('Date: ' + kenh14_item['date'][0] + '\n')
            file.write('Author: ' + kenh14_item['author'][0] + '\n')
            file.write('Tag: ' + kenh14_item['tag'][0] + '\n')


        next_links = self.get_next_links(response)
        print(next_links, "hashkjadshf;kashdf;")
        for link in next_links:
            link = "https://kenh14.vn" + link
            if link not in self.links_set:
                self.links_set.add(link)
                print(link)
                yield scrapy.Request(url = link)


    def get_next_links(self, response):
        return response.css(".visit-popup").xpath("@href").extract()
