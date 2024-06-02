import scrapy
from datetime import datetime

class NetshoesSpider(scrapy.Spider):
    name = "netshoes"
    allowed_domains = ["www.netshoes.com.br"]
    start_urls = ["https://www.netshoes.com.br/running/tenis-performance?genero=masculino"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        # Pegue os links para as páginas dos produtos
        product_links = response.css('a.smarthint-tracking-card::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product)

        # Verifica se deve continuar para a próxima página
        if self.page_count < self.max_pages:
            next_page = response.css('div.pagination a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        
        product_attributes = response.css('ul.attributes li')
        
        if product_attributes:
            brand_element = product_attributes[-1]
            brand = brand_element.css('a::text').get()
        else:
            brand = None

        yield {
            'brand': brand,
            'name': response.css('div.short-showcase-description section.short-description h1::text').get(),
            'new_price_reais': response.css('div.default-price span strong::text').get(),
            'reviews_rating_number': response.css('div.rating-box a span::text').get(),
            'reviews_amount': response.css('div.rating-box a div span.rating-box__numberOfReviews::text').get(),
            'page_count': self.page_count,
            '_source_name': self.name,
            '_source_link': self.start_urls[0],
            '_data_coleta': datetime.now()
        }
