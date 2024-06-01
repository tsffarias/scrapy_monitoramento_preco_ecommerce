import scrapy


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.com.br"]
    start_urls = ["https://shopee.com.br/search?facet=11062129&keyword=tenis%20masculino%20esportivo&noCorrection=true&page=0"]

    def parse(self, response):
        pass
