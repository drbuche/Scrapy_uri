[![N|Solid](https://i.imgur.com/qlKAwfC.jpg)](https://www.urionlinejudge.com.br/)

# Scraping utilizando - Scrapy 

##### Scraping dos ranks da Universidade Regional Integrada. 

# O que é a [URI](https://www.urionlinejudge.com.br/) Online Judge?

A URI Online Judge é um projeto que está sendo desenvolvido pelo Departamento de Ciência da Computação da URI. O principal objetivo é promover a prática de programação e o compartilhamento de conhecimento.

O site contém mais de 1.000 problemas divididos em 8 categorias, todos eles em inglês ou português. Tais categorias auxiliam o aluno a focar nos temas que lhe convêm. Além disso ainda possui suporte para 11 linguagens de programação.

Ao resolver os problemas você acumula pontos e entra no rank de alunos! Caso esteja vinculado a uma instituição de ensino, você pode adicioná-la no seu perfil, fazendo com que a mesma suba de rank com você!

# Etapas do projeto:

Será realizado uma coleta de dados, tendo como base os ranks contidos no site [URI](https://www.urionlinejudge.com.br/). 

- [x] **Coletaremos o [rank de universidades](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_faculdades.py), o qual possui os seguintes atributos:**
    - Rank, Acrônimo_Instituição, Instituição, País, Exercícios_resolvidos e Número_estudantes.
    
- [ ] **Coletaremos o rank de alunos, o qual possui os seguintes atributos:**
    - Rank, Nome_aluno, Acrônimo_Instituição, Pontos e Status.
    
- [x] **Coletaremos o [rank de países](https://github.com/drbuche/Scrapy_uri/blob/master/scrapy/main_paises.py), o qual possui os seguintes atributos:**
    - Rank, País, Sigla, Exercícios_resolvidos e Número_estudantes.

- [ ] **Futuramente montaremos um banco de dados relacional (provavelmente utilizando MySQL).** 
- [ ] **Por fim, será realizada a análise dos dados.**




# Preparando o ambiente:
*\*Os passos com 'ou' representam possíveis soluções para problemas que possam vir a ocorrer, caso a primeira opção não funcione.*
   
   - Atualize o sistema.
   ```sh
sudo apt-get update 
```

   - Atualize o pip.
   ```sh
pip install --upgrade pip 

ou 

pip3 install --upgrade pip
```
  - Instale o Scrapy.
   ```sh
pip install scrapy

ou

pip3 install scrapy
```



# Utilizando!
  - Dentro da pasta 'scrapy_uri', abra o terminal e execute o seguinte comando:
```sh
scrapy runspider main_modulo.py
```
  - Isso mostrará como tudo esta rodando.
  
  - Após isso, digite o comando: 
  
   ```sh
scrapy runspider modulo.py -o modulo.csv
```
  - Isso criara um arquivo .csv, o qual você pode abrir no Excel para organizar e visualizar os dados (lembrando que o scraping é feito de forma não sequencial, então os registros estarão desordenados entre si, não seguindo a sequencia do rank).
  
 
# Dados:

- [Tabela ‘Universidades’ completa .csv – atualizado em Sep/10/2020](https://mega.nz/file/UlczwA5Q#6lXxkdHmXN08O41aDd2_RSEPDLSQJk2BG1kkg97kRLc)
- [Tabela ‘Países’ completa .csv – atualizado em Sep/13/2020](https://mega.nz/file/h5NkTK6D#VwSaCGNB1GjPqWyJGxwrgcdjPHX7LzsU8HR-CZpkxhI)