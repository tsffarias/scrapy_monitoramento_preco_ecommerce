# Projeto de ETL para Monitoramento de Preços e Produtos E-commerce

## Descrição

Imagine que uma marca de tênis deseja avaliar sua relevância no ecossistema do Mercado Livre, Amazon, Magalu, Shopee e Centauro. Para isso, é necessário obter **KPIs** relacionados ao segmento de tênis nessas plataformas. O objetivo é coletar informações detalhadas e implementar um dashboard que facilite a visualização e análise desses dados.

## Proposta do Projeto

Fomos contratados por uma grande empresa para fazer uma pesquisa de mercado na categoria de tênis esportivos dentro de diversos e-commerces: Mercado Livre, Amazon, Magalu, Shopee, Centauro. O objetivo dessa empresa é avaliar:
- 👟 Quais marcas são mais encontradas até a 10ª página
- 💰 Qual o preço médio por marca
- ⭐ Qual a satisfação por marca

## Etapas do Projeto

### Etapa 1: Extração dos Dados
Utilização de **Web Scraping** com a biblioteca **Scrapy** para obter os dados necessários do Mercado Livre, Amazon, Magalu, Shopee, Centauro.

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

## Estrutura de Diretórios

```plaintext
.
├── data
│   ├── data.json
│   └── quotes.db
src/
├── coleta/
│   ├── spiders/
│   │   └── preco_spider.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── transform.py
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
```

### Transformar e carregar os dados

```sh
python src/transformacao/mercado_livre.py
```

### Visualizar Dashboard

```sh
streamlit run dashboard/app.py
```