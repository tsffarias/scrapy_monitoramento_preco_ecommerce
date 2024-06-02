import pandas as pd
import sqlite3
from datetime import datetime
import os
import re

# Definir o caminho relativo para o arquivo JSONL
relative_path_magalu = '../../data/magalu.jsonl'
relative_path_db_magalu = '../../data/quotes.db'

# Obter o caminho absoluto baseado no local do script
jsonl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_magalu))
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_db_magalu))

# Função para limpar e converter preços
def clean_price(price):
    return (price.str.replace(',', '.')
                .str.replace(r'\s+', '', regex=True)
                .str.replace('.', '')
                .str.replace('R$', '')
                .astype(float) / 100)

# Verificar se o arquivo existe
if not os.path.exists(jsonl_path):
    print("Arquivo não encontrado:", jsonl_path)
elif os.stat(jsonl_path).st_size == 0:
    print("O arquivo está vazio:", jsonl_path)
else:
    try:

        # Ler os dados do arquivo JSONL
        df = pd.read_json(jsonl_path, lines=True)

        # Configurar pandas para mostrar todas as colunas
        pd.options.display.max_columns = None

        # Limpar e converter preços
        df['new_price_reais'] = clean_price(df['new_price_reais'])
        df['old_price_reais'] = clean_price(df['old_price_reais'])

        # Tratar os valores nulos para colunas numéricas
        df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
        df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
        df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

        # Tratando a avaliação
        df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

        # Conectar ao banco de dados SQLite (ou criar um novo)
        conn = sqlite3.connect(db_path)

        # Salvar o DataFrame no banco de dados SQLite
        df.to_sql('magalu_items', conn, if_exists='replace', index=False)

        # Fechar a conexão com o banco de dados
        conn.close()

    except ValueError as e:
        print("Erro ao ler o arquivo JSONL:", e)