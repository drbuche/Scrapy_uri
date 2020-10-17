[![N|Solid](https://i.imgur.com/qlKAwfC.jpg)](https://www.urionlinejudge.com.br/)

# Scraping e Análise de Dados.

##### Scraping e análise de dados dos ranks da Universidade Regional Integrada. 

# O que é a [URI](https://www.urionlinejudge.com.br/) Online Judge?

A URI Online Judge é um projeto que está sendo desenvolvido pelo Departamento de Ciência da Computação da URI. O principal objetivo é promover a prática de programação e o compartilhamento de conhecimento.

O site contém mais de 1.000 problemas divididos em 8 categorias, todos eles em inglês ou português. Tais categorias auxiliam o aluno a focar nos temas que lhe convêm. Além disso ainda possui suporte para 11 linguagens de programação.

Ao resolver os problemas você acumula pontos e entra no rank de alunos! Caso esteja vinculado a uma instituição de ensino, você pode adicioná-la no seu perfil, fazendo com que a mesma suba de rank com você!

# Etapas do projeto:

Será realizado uma coleta de dados, tendo como base os ranks contidos no site [URI](https://www.urionlinejudge.com.br/). 

- [x] **Coletaremos o [rank de universidades](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_faculdades.py), o qual possui os seguintes atributos:**
    - Rank, Acrônimo_Instituição, Instituição, País, Exercícios_resolvidos e Número_estudantes.
    
- [x] **Coletaremos o [rank de alunos](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_alunos.py), o qual possui os seguintes atributos:**
    - Rank, Nome_aluno, Acrônimo_Instituição, url_perfil, Pontos e Status.
    
- [x] **Coletaremos o [rank de países](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_paises.py), o qual possui os seguintes atributos:**
    - Rank, País, Sigla, Exercícios_resolvidos e Número_estudantes.
    
- [x] **Coletaremos o [Data_cadastro](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/data_cadastro.py), o qual possui os seguintes atributos:**
    - url_perfil, Data_cadastro.
---
- [x] **Limpar dados.**
    - [Alunos](https://github.com/drbuche/Scrapy_uri/blob/master/jupyter/limpar/limpar_alunos.ipynb)
    - [Países](https://github.com/drbuche/Scrapy_uri/blob/master/jupyter/limpar/limpar_paises.ipynb)
    - [Universidades](https://github.com/drbuche/Scrapy_uri/blob/master/jupyter/limpar/limpar_faculdades.ipynb)

---
    
- [x] **Criar um [banco de dados relacional.](https://github.com/drbuche/Scrapy_uri/blob/master/mysql/uri_database.sql)** 

---

- [ ] **Por fim, será realizada a análise e projeção dos dados.**
    - [Visualizar Folium.Maps - Distribuição de Faculdades](https://nbviewer.jupyter.org/github/drbuche/Scrapy_uri/blob/master/jupyter/trabalhar/heatmap/map_pais.ipynb)
    - [Visualizar Folium.Maps - Distribuição de Alunos](https://nbviewer.jupyter.org/github/drbuche/Scrapy_uri/blob/master/jupyter/trabalhar/heatmap/map_alunos_pais.ipynb) 

### Ferramentas até o momento:
    - Jupyter Notebook
    - Scrapy
    - Numpy
    - Pandas
    - GeoPandas
    - Matplotlib
    - Folium
    - Nominatim


# Preparando o ambiente:
*\*Os passos com 'ou' representam possíveis soluções para problemas que possam vir a ocorrer, caso a primeira opção não funcione.*
   
   - Atualize o sistema.
   ```sh
sudo apt-get update 
```

   - Atualize o pip.
   ```sh
pip install --upgrade pip 
# ou 
pip3 install --upgrade pip
```

  - Instale as dependências:
  
   ```sh
pip install -r requirements.txt
# ou
pip3 install -r requirements.txt
```


# Utilizando o Scrapy!
  - Dentro da pasta 'scrapy_uri', abra o terminal e execute o seguinte comando:
```sh
scrapy runspider main_modulo.py
```
  - Isso mostrará como tudo esta rodando.
  
  - Após isso, digite o comando: 
  
   ```sh
scrapy runspider main_modulo.py -o nome_novo_arquivo.csv
```
  - Isso criara um arquivo .csv, o qual você pode abrir no Excel para organizar e visualizar os dados (lembrando que o scraping é feito de forma não sequencial, então os registros estarão desordenados entre si, não seguindo a sequencia do rank).
  - OBS: O [main_alunos.py](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_alunos.py) retorna um arquivo csv que serve de parâmetro para busca de [data_cadastro.py](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/data_cadastro.py), por esse motivo, execute primeiro o [main_alunos.py](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_alunos.py).
 
# Dados:

### Dados brutos:
- [Tabela ‘Universidades’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/cocTHaJT#9B3NJF6V8BjxzdDrofoDFsDvkQrYKvUWjMc-95QCGuU)
- [Tabela ‘Países’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/F0NUUTAT#_UpNs8G_pQZQCQa37Pqcr9wdqsHpP0sXUsis9twAW3A)
- [Tabela ‘Alunos’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/MgVxzKzT#tzUFrfzno7w5ES8dllJa7RwlLSYZuqBC74AULqXTa8M)
- [Tabela ‘Data_cadastro’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/x1VVyYKT#VkeE8gga2YnroZCrk7LQcQsd0vqEBISG7u1cv_NrGqk)

---
### Dados Limpos:
- [Tabela ‘Universidades’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/4193iSCY#8gPbFU2wmMv-2sPW0tP7-CpIEeiLFslwP8YJ4-EqoaI)
- [Tabela ‘Países’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/Zs9HTITJ#2dgpl_QbW5uxXiaOHZyMTI6pUfT8VO_cVamr6xN6j2M)
- [Tabela ‘Alunos’ completa .csv – atualizado em Oct/06/2020](https://mega.nz/file/dt0HBKDI#rBMJJSXwgU7PlcaYSDBz-Nxz2IpWmj0X44DnnfmbZWU)