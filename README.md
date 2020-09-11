[![N|Solid](https://i.imgur.com/qlKAwfC.jpg)](https://www.urionlinejudge.com.br/)

# Scraping utilizando - Scrapy 

##### Scraping dos ranks da Universidade Regional Integrada. 

Será realizado uma coleta de dados, tendo como base os ranks contidos no site [URI](https://www.urionlinejudge.com.br/). 

- [x] **Coletaremos o rank de universidades, o qual possui os seguintes atributos:**
    - Rank, Acrônimo_Instituição, Instituição, País, Exercícios_resolvidos e Número_estudantes.
    
- [ ] **Coletaremos o rank de alunos, o qual possui os seguintes atributos:**
    - Rank, Nome_aluno, Acrônimo_Instituição, Pontos e Status.
    
- [ ] **Coletaremos o rank de países, o qual possui os seguintes atributos:**
    - Rank, País, Exercícios_resolvidos e Número_estudantes.

- [ ] **Futuramente montaremos um banco de dados relacional (provavelmente utilizando MySQL).** 
- [ ] **Por fim, será realizada a analise dos dados.**




#### Preparando o ambiente:
   - Atualize o pip.
   ```sh
pip install --upgrade pip 
```
  - Instale o Scrapy.
   ```sh
pip install scrapy
```



# Utilizando!
  - Dentro da pasta 'scrapy_uri', abra o terminal e execute o seguinte comando:
```sh
scrapy runspider uri_sc.py
```
  - Isso mostrará como tudo esta rodando.
  
  - Após isso, digite o comando: 
  
   ```sh
scrapy runspider main_faculdades.py -o rank_facul_uri.csv
```
  - Isso criara um arquivo .csv, o qual você pode abrir no Excel para organizar e visualizar os dados (lembrando que o scraping é feito de forma não sequencial, então os registros estarão desordenados entre si, não seguindo a sequencia do rank).
  
  
