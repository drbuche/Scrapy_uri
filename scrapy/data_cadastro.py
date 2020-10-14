import scrapy
from regex import *
import csv


class AlunoInicio(scrapy.Spider):
    name = 'uri'
    start_urls = []
    with open('lista_perfis.csv', newline='') as f:
        reader = csv.reader(f)
        lista_perfis = list(reader)
    for pagina in lista_perfis[0]:
        start_urls.append(f'https://www.urionlinejudge.com.br{pagina}')

        def parse(self, response):
            data_suja = response.xpath('//li[contains(., "Since:")]/text()[2]').getall()
            link = response.xpath(f'//a[contains(@href, "/judge/en/profile/")]/@href').get()
            data = apenas_data(str(data_suja))

            yield {
                'data': data,
                'link': link}
