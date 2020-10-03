import scrapy

class VietnamnetSpider(scrapy.Spider):
    name = 'vietnamnet'
    start_urls = [
        # 'https://vietnamnet.vn/vn/the-thao/bong-da-quoc-te/serie-a/andrea-pirlo-duoc-bo-nhiem-lam-hlv-truong-juventus-664812.html',
        # 'https://vietnamnet.vn/vn/the-thao/bong-da-viet-nam/doi-tuyen-viet-nam/quang-hai-vao-top-500-cau-thu-quan-trong-nhat-the-gioi-664539.html',
        # 'https://vietnamnet.vn/vn/the-thao/hau-truong/arsenal-vs-chelsea-mesut-ozil-tu-huy-hoai-vi-phong-tung-662613.html',
        # 'https://vietnamnet.vn/vn/the-thao/cac-mon-khac/justin-thomas-vo-dich-wgc-fedex-st-jude-invitational-2020-663048.html',
        # 'https://vietnamnet.vn/vn/the-thao/xem-truc-tiep-bong-da/ket-qua-leicester-vs-mu-ket-qua-bong-da-anh-660917.html',

        # 'https://vietnamnet.vn/vn/cong-nghe/cong-dong-mang/giai-cuu-3-nguoi-mac-ket-trong-o-to-giua-dong-lu-cuon-cuon-664795.html',
        # 'https://vietnamnet.vn/vn/cong-nghe/san-pham/5-tinh-nang-cao-cap-cua-galaxy-note20-ultra-5g-664947.html',
        # 'https://vietnamnet.vn/vn/cong-nghe/ung-dung/ung-dung-bluezone-co-tac-dung-gi-663317.html',
        # 'https://vietnamnet.vn/vn/cong-nghe/vien-thong/mang-5g-co-the-mang-lai-hang-nghin-ty-usd-cho-nen-kinh-te-the-gioi-phan-2-trung-quoc-duc-va-nhat-ban-dang-dan-dau-xu-huong-phat-trien-cac-nha-may-thong-minh-661117.html',
        # 'https://vietnamnet.vn/vn/cong-nghe/bao-mat/my-canh-bao-ma-doc-trung-quoc-ton-tai-ca-thap-ky-663557.html',

        # 'https://vietnamnet.vn/vn/phap-luat/ho-so-vu-an/hon-chien-dong-nguoi-hai-anh-em-ruot-bi-chem-trong-thuong-664839.html',
        # 'https://vietnamnet.vn/vn/phap-luat/ky-su-phap-dinh/di-sung-vao-dau-tinh-nhan-va-man-bo-tron-cua-dai-ca-ha-thanh-663472.html',
        # 'https://vietnamnet.vn/vn/phap-luat/tu-van-phap-luat/dich-benh-covid-19-nhung-nguoi-nao-se-dinh-toi-hinh-su-629397.html',

        # 'https://vietnamnet.vn/vn/tuanvietnam/tieudiem/ong-le-kha-phieu-noi-ve-viec-da-tam-thi-phai-goi-dau-664567.html',

        # 'https://vietnamnet.vn/vn/kinh-doanh/tu-van-tai-chinh/vay-1-ty-xay-10-phong-tro-kinh-doanh-ban-thao-tai-san-tra-no-ngan-hang-661723.html',
        # 'https://vietnamnet.vn/vn/kinh-doanh/amaccao/100-chia-khoa-vang-danh-cho-ceo-va-chu-doanh-nghiep-661635.html',
        # 'https://vietnamnet.vn/vn/kinh-doanh/thi-truong/vang-khach-thua-ghe-gia-ve-may-bay-lai-re-beo-664778.html',
        # 'https://vietnamnet.vn/vn/kinh-doanh/doanh-nhan/tien-nhieu-nhu-nu-hoang-mien-tay-tien-lai-tram-ty-it-biet-cua-bau-long-664759.html',
        # 'https://vietnamnet.vn/vn/kinh-doanh/tu-van-tai-chinh/phan-biet-tui-hang-hieu-va-do-fake-664883.html',

        # 'https://vietnamnet.vn/vn/giai-tri/the-gioi-sao/song-hye-kyo-he-lo-ly-do-ly-hon-664788.html',
        # 'https://vietnamnet.vn/vn/giai-tri/thoi-trang/hoa-khoi-ngoai-thuong-nhieu-nguoi-dung-danh-vi-hoa-hau-vao-muc-dich-xau-662055.html',
        # 'https://vietnamnet.vn/vn/giai-tri/nhac/phuong-thanh-nguoi-trong-showbiz-ai-cung-chieu-tro-chi-khac-nhau-muc-dich-664920.html',
        # 'https://vietnamnet.vn/vn/giai-tri/sach/vi-sao-phim-trung-quoc-co-nhieu-san-ngo-ngan-gay-cuoi-664705.html',
        # 'https://vietnamnet.vn/vn/giai-tri/phim/kieu-anh-phia-truoc-la-bau-troi-thong-bao-da-ket-hon-lan-2-664841.html',
        # 'https://vietnamnet.vn/vn/giai-tri/di-san-my-thuat-san-khau/nguyen-tuan-son-hoa-si-dam-me-ve-kieu-664588.html',

        # 'https://vietnamnet.vn/vn/giao-duc/nguoi-thay/pho-chanh-van-phong-bo-gd-dt-dot-tu-tai-bac-kan-663756.html',
        # 'https://vietnamnet.vn/vn/giao-duc/tuyen-sinh/dap-an-mon-toan-ma-de-112-thi-tot-nghiep-thpt-2020-664437.html',
        # 'https://vietnamnet.vn/vn/giao-duc/du-hoc/con-cai-gioi-sieu-giau-trung-quoc-hoc-o-dau-650763.html',
        # 'https://vietnamnet.vn/vn/giao-duc/guong-mat-tre/viet-nam-gianh-huy-chuong-vang-olympic-vat-ly-chau-au-nam-2020-660997.html',
        # 'https://vietnamnet.vn/vn/giao-duc/goc-phu-huynh/hoc-sinh-tp-hcm-nghi-tet-2021-it-hon-nam-ngoai-663961.html',
        # 'https://vietnamnet.vn/vn/giao-duc/hoc-tieng-anh/cach-day-ngoai-ngu-thuan-tu-nhien-cua-ba-me-co-con-thao-8-thu-tieng-650892.html',
        # 'https://vietnamnet.vn/vn/giao-duc/khoa-hoc/nu-sinh-an-do-phat-hien-tieu-hanh-tinh-di-chuyen-ve-trai-dat-663755.html',

        # 'https://vietnamnet.vn/vn/doi-song/gia-dinh/nguoi-me-vo-sinh-nhan-nuoi-2-dua-tre-o-benh-vien-kham-adn-ket-qua-khong-tin-noi-664834.html',
        # 'https://vietnamnet.vn/vn/doi-song/chuyen-la/chuyen-ly-ky-ve-ham-chua-vang-va-noi-kho-cua-nguoi-dan-ong-o-ha-nam-664520.html',
        # 'https://vietnamnet.vn/vn/doi-song/gioi-tre/de-hoa-dong-voi-moi-nguoi-hay-nho-ba-cau-nay-la-du-663802.html',
        # 'https://vietnamnet.vn/vn/doi-song/tam-su/met-moi-vi-mau-thuan-voi-me-chong-664821.html',
        # 'https://vietnamnet.vn/vn/doi-song/du-lich/ban-lang-moc-mac-nho-xinh-o-sa-pa-khien-ai-cung-muon-ghe-tham-664822.html',
        # 'https://vietnamnet.vn/vn/doi-song/am-thuc/cach-lam-nom-cu-dau-thanh-mat-chua-ngot-664221.html',
        # 'https://vietnamnet.vn/vn/doi-song/meo-vat/5-meo-giup-khu-mui-am-moc-tren-quan-ao-vao-mua-mua-664559.html',

        # 'https://vietnamnet.vn/vn/bat-dong-san/du-an/bien-dat-cong-vien-van-hoa-thanh-xuong-go-bai-xe-container-664704.html',
        # 'https://vietnamnet.vn/vn/bat-dong-san/noi-that/5-mau-phong-thay-do-dep-den-xieu-long-cho-phong-ngu-nho-nhin-thoi-la-chi-muon-decor-ngay-656970.html',
        # 'https://vietnamnet.vn/vn/bat-dong-san/thi-truong/quan-vung-ven-tp-hcm-cong-khai-vi-pham-xay-dung-tren-mang-xa-hoi-662631.html',
        # 'https://vietnamnet.vn/vn/bat-dong-san/tam-diem/bo-xay-dung-co-de-xuat-moi-ve-kinh-phi-2-bao-tri-nha-chung-cu-664661.html',
        
        # 'https://vietnamnet.vn/vn/ban-doc/hoi-am/khong-can-dong-bhxh-cho-nld-nuoc-ngoai-ky-hop-dong-duoi-12-thang-664475.html',
        # 'https://vietnamnet.vn/vn/ban-doc/chia-se/con-trai-ung-thu-con-gai-viem-ruot-gia-dinh-ngheo-lam-vao-duong-cung-664390.html',
        # 'https://vietnamnet.vn/vn/ban-doc/tho/thuong-lam-canh-co-oi-663366.html',
        # 'https://vietnamnet.vn/vn/ban-doc/hoi-am/dieu-le-moi-cua-facebook-dung-tuyen-bo-coi-kho-664918.html',

        # 'https://vietnamnet.vn/vn/oto-xe-may/kham-pha/o-to-bo-hoang-47-nam-tuoi-bong-choc-ban-duoc-gan-7-ty-662656.html',
        # 'https://vietnamnet.vn/vn/oto-xe-may/dien-dan/ra-duong-am-anh-ninja-viet-nam-662407.html',
        # 'https://vietnamnet.vn/vn/oto-xe-may/danh-gia-xe/mitsubishi-xpander-va-honda-br-v-so-gang-tai-malaysia-664465.html',
        # 'https://vietnamnet.vn/vn/oto-xe-may/gia-xe/them-hang-loat-mau-xe-giam-gia-toi-tram-trieu-dau-thang-8-663777.html',
        # 'https://vietnamnet.vn/vn/oto-xe-may/sau-tay-lai/quen-keo-phanh-tay-bi-cua-oto-kep-trung-664683.html',
        # 'https://vietnamnet.vn/vn/oto-xe-may/xe-moi/mo-lien-doanh-tai-trung-quoc-hang-xe-my-bi-an-cap-het-thiet-ke-663832.html',
        'https://vietnamnet.vn/vn/oto-xe-may/tu-van/nhung-cong-nghe-an-toan-cuu-canh-cho-lai-xe-trong-mua-mua-663136.html',
        'https://vietnamnet.vn/vn/thoi-su/chinh-tri/nguyen-tong-bi-thu-le-kha-phieu-tam-guong-cong-hien-het-minh-664388.html',
        
        # 'https://vietnamnet.vn/vn/suc-khoe/khong-can-lam-gi-chi-thay-doi-gio-an-cung-giup-ban-giam-can-658587.html',
        # 'https://vietnamnet.vn/vn/suc-khoe/5-dau-hieu-khi-hut-thuoc-canh-bao-ung-thu-phoi-xuat-hien-661212.html',
        # 'https://vietnamnet.vn/vn/suc-khoe/nam-thanh-nien-khoe-manh-bong-nhien-mat-giong-noi-664745.html',

        # 'https://vietnamnet.vn/vn/the-gioi/binh-luan-quoc-te/trung-quoc-tuyen-bo-khong-dinh-the-ngoi-sieu-cuong-my-664273.html',
        # 'https://vietnamnet.vn/vn/the-gioi/chan-dung/trang2/',
        # 'https://vietnamnet.vn/vn/the-gioi/ho-so/trung-quoc-se-ra-sao-neu-tham-hoa-ap-xuong-song-duong-tu-664044.html',
        # 'https://vietnamnet.vn/vn/the-gioi/the-gioi-do-day/tu-in-sec-gia-nguoi-dan-ong-my-mua-duoc-sieu-xe-porsche-664881.html',
        # 'https://vietnamnet.vn/vn/the-gioi/viet-nam-va-the-gioi/',
        # 'https://vietnamnet.vn/vn/the-gioi/quan-su/dieu-xay-ra-truoc-khi-xe-boc-thep-my-chim-khien-8-quan-nhan-chet-tham-664414.html',

        # 'https://vietnamnet.vn/vn/thoi-su/chong-tham-nhung/ky-luat-6-uy-vien-nguyen-uy-vien-bo-chinh-tri-trung-uong-trong-nua-nam-660745.html',
        # 'https://vietnamnet.vn/vn/thoi-su/quoc-hoi/bo-truong-cong-an-sot-ruot-khi-vang-bong-2-du-an-luat-cua-nganh-658171.html',
        # 'https://vietnamnet.vn/vn/thoi-su/an-toan-giao-thong/',
        # 'https://vietnamnet.vn/vn/thoi-su/bhxh-bhyt/giam-sat-thuc-hien-chinh-sach-bhxh-bhyt-tai-lang-son-476586.html',

        #'https://vietnamnet.vn/vn/thoi-su/bhxh-bhyt/giam-sat-thuc-hien-chinh-sach-bhxh-bhyt-tai-lang-son-476586.html'
    ]
    file = open("/home/straw/Data_mining/Technical_Tutorial/Scrapy/news/vietnamnet.txt", "a")

    def parse(self, response):
        tag = response.css('.top-cate-head-title a::text').extract()
        title = response.css('h1::text').extract() 
        date = response.css('.ArticleDate::text').extract()
        summary = response.css('.bold.ArticleLead p::text').extract()

        #print(tag, title, date, summary, "bbbbbbbbbbbbbbbbbbbbbbb")
        if len(summary) == 0: summary.append("___")

        self.file.write(str(tag[0]) + '|' + str(date[0][0:10]) + '|' + str(title[0]) + '|' + str(summary[0]) + '\n')

        next_links = self.get_next_links(response)
        for link in next_links:
            link = "https://vietnamnet.vn" + link 
            #print(link)
            yield scrapy.Request(link)


    def get_next_links(self, response):
        return response.css('a.f-18::attr(href)').extract() 

