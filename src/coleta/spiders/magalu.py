import scrapy
from datetime import datetime

class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/tenis%2Bmasculino/?from=clickSuggestion&filters=category---ES%2Bsubcategory---ELNN"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        
        products = response.css("div.sc-fqkvVR.sc-fBWQRz")

        for product in products:
            prices = product.css('::text').getall()
            
            print(prices)
            '''
            yield {
                'brand': product.css('::text').get(),
                'name': product.css('::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'reviews_rating_number': product.css('::text').get(),
                'reviews_amount': product.css('::text').get(),
                'page_count': self.page_count,
                '_source_name': self.name,
                '_source_link': self.start_urls[0],
                '_data_coleta': datetime.now()
            }
            '''

