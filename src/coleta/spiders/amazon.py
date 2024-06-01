import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amzn.to"]
    start_urls = ["https://amzn.to/3Vl7Wii"]

    def parse(self, response):
        pass
