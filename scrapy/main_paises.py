import scrapy
from regex import *


class UriRank(scrapy.Spider):
    name = 'uri'
    start_urls = []
    for pagina in range(1, 11):
        start_urls.append(f'https://www.urionlinejudge.com.br/judge/pt/countries?page={pagina}&direction=DESC')

    def parse(self, response):

        rankbruto = response.xpath('//tbody//tr//td//a/text()').getall()
        ranknumerobruto = response.xpath('//tbody//tr//td[@class="id"][1]/text()').getall()
        resolvidosbruto = response.xpath('//tbody//tr//td[@class="id"][3]/text()').getall()
        estudantebruto = response.xpath('//tbody//tr//td[@class="id"][4]/text()').getall()
        contadorfixo = -1
        for loop in range(0, len(rankbruto), 2):
            sigla = None
            n_pais = None
            ranknumero = None
            resolvido = None
            estudantes = None

            sigla = rankbruto[loop]
            n_pais = rankbruto[loop + 1]
            contadorfixo += 1
            try:
                pais = rankbruto[contadorfixo].replace('flag flag-', '')
            except:
                pais = 'NA'
            ranknumero = int(ranknumerobruto[contadorfixo])
            resolvido = remove_quenbr_rp(resolvidosbruto[contadorfixo])
            estudantes = remove_quenbr_rp(estudantebruto[contadorfixo])

            yield {
                'rank': ranknumero,
                'sigla': sigla,
                'pais': n_pais,
                'resolvidos': resolvido,
                'estudantes': estudantes

            }
