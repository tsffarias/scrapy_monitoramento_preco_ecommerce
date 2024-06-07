import pandas as pd
import sqlite3
from datetime import datetime
import os

# Definir o caminho relativo para o arquivo JSONL
relative_path_mercado_livre = '../../data/mercado_livre.jsonl'
relative_path_db_mercado_livre = '../../data/quotes.db'

# Obter o caminho absoluto baseado no local do script
jsonl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_mercado_livre))
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_db_mercado_livre))

# Verificar se o arquivo existe
if not os.path.exists(jsonl_path):
    print("Arquivo não encontrado:", jsonl_path)
elif os.stat(jsonl_path).st_size == 0:
    print("O arquivo está vazio:", jsonl_path)
else:
    try:

        # Ler os dados do arquivo JSONL
        df = pd.read_json(jsonl_path, lines=True)

        # Tratar os valores nulos para colunas numéricas e de texto
        df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
        df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
        df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
        df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
        df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

        # Remover os parênteses das colunas `reviews_amount`
        df['reviews_amount'] = df['reviews_amount'].str.replace(r'[\(\)]', '', regex=True)
        df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

        # Tratar os preços como floats e calcular os valores totais
        df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
        df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

        # Remover as colunas antigas de preços
        df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)
        
        # Conectar ao banco de dados SQLite (ou criar um novo)
        conn = sqlite3.connect(db_path)

        # Salvar o DataFrame no banco de dados SQLite
        df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

        # Fechar a conexão com o banco de dados
        conn.close()
        
        # Configurar pandas para mostrar todas as colunas
        pd.options.display.max_columns = None

    except ValueError as e:
        print("Erro ao ler o arquivo JSONL:", e)
