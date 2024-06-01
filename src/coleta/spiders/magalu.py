import scrapy


class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/tenis%2Bmasculino/?from=clickSuggestion&filters=category---ES%2Bsubcategory---ELNN"]

    def parse(self, response):
        pass
