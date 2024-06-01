import scrapy
from datetime import datetime
import re

class CentauroSpider(scrapy.Spider):
    name = "centauro"
    allowed_domains = ["www.centauro.com.br"]
    start_urls = ["https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness/genero/masculino"]
    page_count = 1
    max_page = 10

    def parse(self, response):
        
        products = response.css('a.ProductCard-styled__Card-sc-bbe8eefb-0.kOXydP')
        for product in products:
            # Extraindo a avaliação do texto
            rating_div = product.css('div[data-testid="product-rating"]::attr(aria-label)').get()
            rating = None
            if rating_div:         
                match = re.search(r'avaliado em (\d+(\.\d+)?) de 5 estrelas', rating_div)
                if match:
                    rating = match.group(1)
            
            yield {
                'brand': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split(" ")[1],
                'name': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split("-")[0],
                'old_price_reais': product.css('del.Typographystyled__Offer-sc-bdxvrr-4.cAyLkZ.Price-styled__OldPriceOffer-sc-f65c9c0d-2.hLWMiV::text').get(),
                'new_price_reais': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.eFDcLB.Price-styled__CurrentPrice-sc-f65c9c0d-4.jNAhVm::text').get(),
                'reviews_rating_number': rating,
                'page_count': self.page_count,
                '_source_name': self.name,
                '_source_link': self.start_urls[0],
                '_data_coleta': datetime.now()
            }
        

        if self.page_count < self.max_page:
            next_page = f"{self.start_urls[0]}?page={self.page_count}"
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
