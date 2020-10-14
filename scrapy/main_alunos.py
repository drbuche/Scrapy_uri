import scrapy
from regex import *
import os


class UriRank(scrapy.Spider):
    name = 'uri'
    start_urls = []
    url_alunos_perfil = []

    for pagina in range(1, 11740):
        start_urls.append(f'https://www.urionlinejudge.com.br/judge/en/rank?page={pagina}')

        def parse(self, response):
            rankbruto = response.xpath('//tbody//tr//td//a/text()').getall()
            paisbruto = response.xpath('//tbody//tr//td//div/@class').getall()
            pontosbruto = response.xpath('//tbody//tr//td[@class="small"][2]/text()').getall()
            estudante_status = response.xpath('//span[contains(@class, "alive")]/@class').getall()
            link_perfil = response.xpath('//a[contains(@href, "/judge/en/profile")]/@href').getall()
            contadorfixo = -1


            for loop in range(0, len(rankbruto), 2):
                naluno = None
                sigla = None
                pais = None
                pontos = None
                aluno_status = None
                inicio = None

                naluno = rankbruto[loop]
                try:
                    sigla = rankbruto[loop + 1]
                except:
                    sigla = '-'
                contadorfixo += 1
                pontos = apenas_pontos_float(pontosbruto[contadorfixo])
                aluno_status = estudante_status[contadorfixo]
                try:
                    pais = apenas_sigla_pais(paisbruto[contadorfixo])
                except:
                    pais = 'NaN'
                self.url_alunos_perfil.append(link_perfil[contadorfixo])

                yield {
                    'pontos': float(pontos),
                    'nome_aluno': naluno,
                    'faculdade_sigla': sigla,
                    'pais': pais,
                    'perfil': link_perfil[contadorfixo],
                    'status': aluno_status,

                }

    def __del__(self):  # Chave Primária / Chave estrangeira usada para conectar a tabela de "Data_cadastro"
        lista_perfis = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lista_perfis.csv'), "w")
        lista_perfis.writelines(','.join(self.url_alunos_perfil))
        lista_perfis.close()
