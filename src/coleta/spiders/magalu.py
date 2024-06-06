import scrapy
from datetime import datetime

class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/tenis%2Bmasculino/?from=clickSuggestion&filters=category---ES%2Bsubcategory---ELNN"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        # Pegue os links para as páginas dos produtos
        product_links = response.css('a.sc-eBMEME::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)

        # Verifica se deve continuar para a próxima página
        '''
        if self.page_count < self.max_pages:
            self.page_count += 1
            next_page = self.start_urls[0] + f'&page={self.page_count}'
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse)
        '''

    def parse_product(self, response):

        yield {
            'brand': response.css('a[data-testid=heading-product-brand]::text').get(),
            'name': response.css('h1[data-testid=heading-product-title]::text').get(),
            'new_price_reais': response.css('p[data-testid=price-value]::text').get(),
            'old_price_reais': response.css('p[data-testid=price-original]::text').get(),
            'reviews_rating_number': response.css('span[data-testid=review-totalizers-rating]::text').get(),
            'reviews_amount': response.css('p[data-testid=review-totalizers-count]::text').get(),
            'page_count': self.page_count,
            '_source_name': self.name,
            '_source_link': self.start_urls[0],
            '_data_coleta': datetime.now()
        }