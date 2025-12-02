import scrapy 
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem


class GoodReadsSpider(scrapy.Spider):
    name = 'quotebot'

    def start_requests(self):
        urls = ["https://www.goodreads.com/quotes?page=1"]

        for url in urls: 
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):

        for elemento in response.xpath("//div[@class ='quote']"):
            loader = ItemLoader(item=CitacaoItem(),selector=elemento,response=response)

            loader.add_xpath('frase',".//div[@class = 'quoteText']/text()")
            loader.add_xpath('autor',".//span[@class = 'authorOrTitle']/text()")
            loader.add_xpath('tags',".//div[@class='greyText smallText left']/a/text()")

            yield loader.load_item()
           
   

        numero_proximo =  response.xpath("//a[@class='next_page']/@href").get().split('=')[1]
        print("#"*50)
        print(numero_proximo)
        print("#"*50)
        if numero_proximo is not None:

            link_proximo = f'https://www.goodreads.com/quotes?page={numero_proximo}'
            print("#"*50)
            print(link_proximo)
            print("#"*50)

            yield scrapy.Request(url=link_proximo,callback=self.parse)

     


