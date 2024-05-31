import scrapy
from datetime import datetime

class CentauroSpider(scrapy.Spider):
    name = "centauro"
    allowed_domains = ["www.centauro.com.br"]
    start_urls = ["https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness/genero/masculino"]
    pagina_atual = 1
    max_page = 10

    def parse(self, response):
        
        products = response.css('a.ProductCard-styled__Card-sc-bbe8eefb-0.kOXydP')
        for product in products:
            yield {
                'name': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split("-")[0],
                'brand': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.knvuZc.ProductCard-styled__Title-sc-bbe8eefb-3.fnPvPK::text').get().split(" ")[1],
                'last_price': product.css('del.Typographystyled__Offer-sc-bdxvrr-4.cAyLkZ.Price-styled__OldPriceOffer-sc-f65c9c0d-2.hLWMiV::text').get(),
                'current_price': product.css('p.Typographystyled__Paragraph-sc-bdxvrr-1.eFDcLB.Price-styled__CurrentPrice-sc-f65c9c0d-4.jNAhVm::text').get(),
                'page_count': self.pagina_atual,
                '_source_name': self.name,
                '_source_link': self.start_urls[0],
                '_data_coleta': datetime.now()
            }
        

        if self.pagina_atual < self.max_page:
            next_page = f"{self.start_urls[0]}?page={self.pagina_atual}"
            if next_page:
                self.pagina_atual += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
