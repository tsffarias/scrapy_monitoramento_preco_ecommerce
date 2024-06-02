import scrapy
from datetime import datetime


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.com.br"]
    start_urls = ["https://shopee.com.br/search?facet=11062129&keyword=tenis%20masculino%20esportivo&noCorrection=true&page=0"]
    page_count = 1
    max_pages = 10

    #response.xpath('//*[@id="item-list"]/div[1]/a[1]/div/div[2]/div[1]/span/text()').get() netshoes
    #test = response.xpath('//*[@id="item-list"]/div[1]')
    #test.get()
    #test.css('div.item-card__description__product-name').get()
    #len(test.css('a.smarthint-tracking-card')) -- aqui eu consegue pegar 42 tenis 
    # test.css('a.smarthint-tracking-card')[0].get()
    # test.css('a.smarthint-tracking-card div.item-card__description__product-name span::text')[0].get() -- nome produto
    # 

    def parse(self, response):
        
        products = response.css("li.shopee-search-item-result__item")

        for product in products:
            prices = product.css('div._1Mfhcw.hVNzu-.G+ZP8F::text').getall()
            
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
