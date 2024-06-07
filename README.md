# Projeto de ETL para Monitoramento de Preços e Produtos E-commerce

## Descrição

Imagine que uma marca de tênis deseja avaliar sua relevância no ecossistema do Mercado Livre e Centauro. Para isso, é necessário obter **KPIs** relacionados ao segmento de tênis nessas plataformas. O objetivo é coletar informações detalhadas e implementar um dashboard que facilite a visualização e análise desses dados.

## Proposta do Projeto

Fomos contratados por uma grande empresa para fazer uma pesquisa de mercado na categoria de tênis esportivos dentro de diversos e-commerces: Mercado Livre e Centauro. O objetivo dessa empresa é avaliar:
- 👟 Quais marcas são mais encontradas até a 10ª página
- 💰 Qual o preço médio por marca
- ⭐ Qual a satisfação por marca

# Fontes de Dados
- Mercado Livre
- Centauro

## Etapas do Projeto

### Etapa 1: Extração dos Dados
Utilização de **Web Scraping** com a biblioteca **Scrapy** para obter os dados necessários do Mercado Livre e Centauro.

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
![dashboard](/pics/mercado_livre.png)

## Estrutura de Diretórios

```plaintext
.
data/
│── centauro.jsonl
│── mercado_livre.jsonl
│── quotes.db
pics/
│── arquitetura.png
src/
├── coleta/
│   ├── spiders/
│   │   └── centauro.py
│   │   └── mercadolivre.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── centauro.py
│   ├── mercadolivre.py
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
```

### Transformar e carregar os dados

```sh
python src/transformacao/mercado_livre.py
python src/transformacao/centauro.py
```

### Visualizar Dashboard

```sh
streamlit run src/dashboard/app.py
```

## Análise dos Dados do dia 07/06/2024

### 📊 Análise Descritiva dos Dados

#### Mercado Livre:
- **Marcas mais comuns**:
  - **Olympikus**: 148 produtos
  - **Mizuno**: 40 produtos
  - **Fila**: 29 produtos

- **Preço médio por marca**:
  - **MVP FITNESS**: R$ 360,00
  - **FILA**: R$ 301,38
  - **NEW BALANCE**: R$ 257,47
  - **PUMA**: R$ 256,85
  - **QIX**: R$ 237,00
  - **UNDER ARMOUR**: R$ 223,77
  - **ADIDAS**: R$ 216,40
  - **MIZUNO**: R$ 214,21
  - **N&W**: R$ 189,00
  - **MZ**: R$ 183,50

- **Satisfação por marca (por maior número de quantidade de avaliação)**:
  - **OLYMPIKUS**: 4,73 e quantidade de avaliações: 119
  - **MIZUNO**: 4,59 e quantidade de avaliações: 28
  - **FILA**: 4,78 e quantidade de avaliações: 25

#### Centauro:
- **Marcas mais comuns**:
  - **Olympikus**: 104 produtos
  - **Everlast**: 76 produtos
  - **Under Armour**: 73 produtos

- **Preço médio por marca**:
  - **New Balance**: R$ 974
  - **Reebok**: R$ 697
  - **Nike**: R$ 582
  - **Asics**: R$ 448
  - **Adidas**: R$ 414
  - **Armour**: R$ 399
  - **Bull**: R$ 399
  - **Under Armour**: R$ 388
  - **Skechers**: R$ 323

- **Satisfação por marca (por maior número de quantidade de avaliação)**:
  - **Nike**: 4,00 e quantidade de avaliações: 18
  - **Olympikus**: 4,62 e quantidade de avaliações: 7
  - **Under Armour**: 3,60 e quantidade de avaliações: 5


### 💡 Insights Relevantes:

1. **Marcas Mais Comuns**:
   - **Mercado Livre**: A marca Olympikus é a mais comum com 148 produtos, seguida por Mizuno com 40 produtos e Fila com 29 produtos.
   - **Centauro**: A Olympikus também lidera com 104 produtos, seguida por Everlast com 76 produtos e Under Armour com 73 produtos.

2. **Preço Médio por Marca**:
   - **Mercado Livre**: As marcas com os preços médios mais altos são MVP FITNESS (R$ 360,00), FILA (R$ 301,38) e NEW BALANCE (R$ 257,47).
   - **Centauro**: As marcas com os preços médios mais altos são New Balance (R$ 974), Reebok (R$ 697) e Nike (R$ 582).

3. **Satisfação por Marca (com base na quantidade de avaliações)**:
   - **Mercado Livre**: A Olympikus possui uma alta satisfação com uma média de 4,73 (119 avaliações), seguida por Mizuno com uma média de 4,59 (28 avaliações) e Fila com uma média de 4,78 (25 avaliações).
   - **Centauro**: A Nike tem uma média de satisfação de 4,00 com 18 avaliações, Olympikus com 4,62 e 7 avaliações, e Under Armour com 3,60 e 5 avaliações.

Esses insights mostram que a Olympikus é uma marca muito presente e bem avaliada em ambas as plataformas, indicando uma forte aceitação no mercado. As marcas com preços mais altos no Mercado Livre são MVP FITNESS, FILA e NEW BALANCE, enquanto na Centauro, as marcas mais caras são New Balance, Reebok e Nike, o que pode indicar uma diferenciação no mercado de produtos premium. A satisfação média elevada de marcas como Olympikus, Mizuno e Fila no Mercado Livre, e Nike e Olympikus na Centauro, sugere uma boa aceitação dos consumidores.

Essas análises fornecem uma visão clara das tendências de mercado e preferências do consumidor nos e-commerces analisados, permitindo que a marca de tênis avalie sua relevância e competitividade no mercado.

## Melhorias Futuras no Projeto
- Adicionar mais fontes de dados: Magalu, Netshoes e Amazon