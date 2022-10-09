from itertools import count
import scrapy
import pandas as pd
import openpyxl
 
class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['ooyyo.com']
    headers_ooyyo = {
            "DNT": "1","Host": "www.ooyyo.com","Sec-GPC": "1","TE": "trailers",
            "Pragma": "no-cache","Referer": "https://www.ooyyo.com/",
            "Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
            "X-KL-Ajax-Request": "Ajax_Request","X-Niobe-Short-Circuited": "true"
        }
   
    def start_requests(self):
        url = f"https://www.ooyyo.com/denmark/used-cars-for-sale/c=CDA31D7114D3854F111B9E6FAA651453/"
 
        yield scrapy.Request(
            url=url,
            method='GET',
            headers=self.headers_ooyyo,
            callback=self.initial_parse,
        )

    loop = 0
    count=0
    def initial_parse(self, response):
        next_page_url = response.xpath("//div[@class='resultset']/a/@href").getall() 
        if next_page_url:
            self.loop=len(next_page_url)
            for page in next_page_url:
                absolute_next_page_url = response.urljoin(page)
                yield scrapy.Request(
                    url=absolute_next_page_url,
                    method='GET',
                    headers=self.headers_ooyyo,
                    callback=self.basic_info_parse,
                    dont_filter=True
                )
           

    title = []
    data = []
    def basic_info_parse(self, response):
        info = response.xpath("//li/div/span[@class='_js-hook-main-price']/text()").extract_first('').strip()
        if info:
            try:
                priceMeta = response.xpath("//meta[@name='description']/@content")[0].extract()
                t_price = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[0]
                price=priceMeta.split(", ")[2]
                t_make = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[2]
                make = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[3]
                t_model = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[4]
                model = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[5]
                t_trim = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[6]
                trim = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[7]
                t_mi = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[8]
                mi = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[9]
                t_year = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[10]
                year = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[11]
                t_fuel = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[12]
                fuel = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[13]
                t_body = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[14]
                body = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[15]
                t_color = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[16]
                color = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[17]
                t_city = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[18]
                city = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[19]
                t_power = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[20]
                power = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[21]
                t_transmission = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[22]
                transmission = response.xpath("//ul[@class='basic-info']/li/div/text()").extract()[23]

                options = response.xpath("//ul[@class='options']/li/text()").extract()
                options= list(map(lambda x:x.strip(),options))
                options= list(filter(None, options))

                contact_page_url = response.xpath("//a[@class='btn btn-lg btn-warning btn-contact d-none d-lg-block w-p100']/@href").extract_first()

                self.data.append([price, make, model, trim, mi, year, fuel, body, color, city, power, transmission, contact_page_url]) 
                self.title = [t_price, t_make, t_model, t_trim, t_mi, t_year, t_fuel, t_body, t_color, t_city, t_power, t_transmission, "Contact Seller"]

            except IndexError:
                pass

            self.count+=1
            if self.count==self.loop :
                df = pd.DataFrame(self.data, columns=self.title)

                df.to_excel('pandas_to_excel.xlsx', sheet_name='data_sheet')

            yield None
                
 