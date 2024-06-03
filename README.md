# Projeto de ETL para Monitoramento de Preços e Produtos E-commerce

## Descrição

Imagine que uma marca de tênis deseja avaliar sua relevância no ecossistema do Mercado Livre, Magalu, Centauro e Netshoes. Para isso, é necessário obter **KPIs** relacionados ao segmento de tênis nessas plataformas. O objetivo é coletar informações detalhadas e implementar um dashboard que facilite a visualização e análise desses dados.

## Proposta do Projeto

Fomos contratados por uma grande empresa para fazer uma pesquisa de mercado na categoria de tênis esportivos dentro de diversos e-commerces: Mercado Livre, Magalu, Centauro e Netshoes. O objetivo dessa empresa é avaliar:
- 👟 Quais marcas são mais encontradas até a 10ª página
- 💰 Qual o preço médio por marca
- ⭐ Qual a satisfação por marca

# Fontes de Dados
- Mercado Livre
- Magalu
- Centauro
- Netshoes

## Etapas do Projeto

### Etapa 1: Extração dos Dados
Utilização de **Web Scraping** com a biblioteca **Scrapy** para obter os dados necessários do Mercado Livre, Magalu, Centauro e Netshoes.

### Etapa 2: Transformação dos Dados
Processamento e limpeza dos dados utilizando a biblioteca **Pandas** para garantir que estejam prontos para análise.

### Etapa 3: Carregamento dos Dados
Armazenamento dos dados transformados em um banco de dados **SQLite3**.

### Etapa 4: Visualização dos Dados
Desenvolvimento de um **dashboard interativo** usando **Streamlit** para consumir os dados e apresentar os insights de forma visual e intuitiva.

## Ferramentas Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do projeto.
- **Pandas**: Biblioteca utilizada para manipulação e transformação de dados.
- **Scrapy**: Framework utilizado para realizar o web scraping e extrair dados da web.
- **Streamlit**: Framework utilizado para criar aplicações web interativas e visualizar os dados extraídos.
- **SQLite3**: Banco de dados utilizado para armazenar os dados transformados.

### Diagrama

![arquitetura](/pics/arquitetura.png)

### Dashboard
- Link dashboard: (Adicionar link Aqui)

![dashboard](/pics/mercado_livre.png)

## Estrutura de Diretórios

```plaintext
.
data/
│── centauro.jsonl
│── mercado_livre.jsonl
│── magalu.jsonl
│── netshoes.jsonl
│── quotes.db
pics/
│── arquitetura.png
src/
├── coleta/
│   ├── spiders/
│   │   └── centauro.py
│   │   └── mercadolivre.py
│   │   └── magalu.py
│   │   └── netshoes.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── centauro.py
│   ├── mercadolivre.py
│   ├── magalu.py
│   ├── netshoes.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md
```

## Como Executar o Projeto

Primeiramente, acesse a pasta do projeto e instale as dependências usando o `pip` ou o `Poetry`. Para isso, execute um dos comandos abaixo:

```sh
poetry install
```

ou

```sh
pip install -r requirements.txt
```

Em seguida, para executar cada etapa, siga as instruções abaixo:

### Extração dos dados usando Web Scraping

```sh
cd src/coleta/
scrapy crawl mercadolivre -o ../../data/mercado_livre.jsonl
scrapy crawl centauro -o ../../data/centauro.jsonl
scrapy crawl magalu -o ../../data/magalu.jsonl
scrapy crawl netshoes -o ../../data/netshoes.jsonl
```

### Transformar e carregar os dados

```sh
python src/transformacao/mercado_livre.py
python src/transformacao/centauro.py
python src/transformacao/magalu.py
python src/transformacao/netshoes.py
```

### Visualizar Dashboard

```sh
streamlit run src/dashboard/app.py
```

## Análise dos Dados do dia 02/06/2024

Análise dos dados aqui após extração dos dados