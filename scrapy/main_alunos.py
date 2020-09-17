import scrapy
from regex import *


class UriRank(scrapy.Spider):
    name = 'uri'
    start_urls = []
    for pagina in range(1, 11609):
        start_urls.append(f'https://www.urionlinejudge.com.br/judge/pt/rank?page={pagina}')

        def parse(self, response):

            rankbruto = response.xpath('//tbody//tr//td//a/text()').getall()
            paisbruto = response.xpath('//tbody//tr//td//div/@class').getall()
            pontosbruto = response.xpath('//tbody//tr//td[@class="small"][2]/text()').getall()
            estudante_status = response.xpath('//tbody//tr//td//span/@class').getall()
            contadorfixo = -1
            for loop in range(0, len(rankbruto), 2):
                naluno = None
                sigla = None
                pais = None
                pontos = None
                aluno_status = None

                naluno = rankbruto[loop]
                try:
                    sigla = rankbruto[loop + 1]
                except:
                    sigla = '-'
                contadorfixo += 1
                pontos = remove_quenbr_rpvp(pontosbruto[contadorfixo])
                aluno_status = estudante_status[contadorfixo]
                try:
                    pais = paisbruto[contadorfixo].replace('flag flag-', '')
                except:
                    pais = 'NA'

                yield {
                    'pontos': float(pontos),
                    'nome_aluno': naluno,
                    'faculdade_sigla': sigla,
                    'pais': pais,
                    'status': aluno_status

                }

