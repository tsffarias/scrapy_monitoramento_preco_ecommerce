import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px

class Dashboard:

    def __init__(self):
        df = self.connect_db()
        self.dashboard(df)

    def connect_db(self):
        relative_path_db_mercado_livre = '../../data/quotes.db'
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_db_mercado_livre))

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)

        # Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
        df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

        # Fechar a conexão com o banco de dados
        conn.close()
        
        return df

    def dashboard(self, df):
        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

        # Melhorar o layout com colunas para KPIs
        st.subheader("KPIs Principais")
        col1, col2, col3 = st.columns(3)

        # KPI 1: Número total de itens
        total_items = df.shape[0]
        col1.metric(label="Número Total de Itens", value=total_items)

        # KPI 2: Número de marcas únicas
        unique_brands = df['brand'].nunique()
        col2.metric(label="Número de Marcas Únicas", value=unique_brands)

        # KPI 3: Preço médio novo (em reais)
        average_new_price = df['new_price'].mean()
        col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

        st.divider()

        # Quais marcas são mais encontradas até a 10ª página
        st.subheader('Marcas mais encontradas até a 10ª página')
        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = (df['brand']
                                    .value_counts()
                                    .nlargest(10)
                                    .sort_values(ascending=False)
                                    .to_frame()
                                    .reset_index())
        top_10_pages_brands.columns = ['marca', 'contagem']
        fig = px.bar(top_10_pages_brands, x='marca', y='contagem', text_auto='.2s')
        top_10_pages_brands_table = df['brand'].value_counts().sort_values(ascending=False)
        
        col1.plotly_chart(fig)
        col2.write(top_10_pages_brands_table)

        st.divider()

        # Qual o preço médio por marca
        st.subheader('Preço médio por marca')
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = (df.groupby('brand')['new_price']
                                        .mean()
                                        .nlargest(10)
                                        .sort_values(ascending=False)
                                        .to_frame()
                                        .reset_index())
        average_price_by_brand.columns = ['marca', 'preco_medio_novo']
        fig1 = px.bar(average_price_by_brand, x='marca', y='preco_medio_novo', text_auto='.2s')
        average_price_by_brand_table = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig1)
        col2.write(average_price_by_brand_table)

        st.divider()

        # Qual a satisfação por marca
        st.subheader('Satisfação por marca')
        col1, col2 = st.columns([4, 2])
        df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
        satisfaction_by_brand = (df_non_zero_reviews
                                        .groupby('brand')
                                        ['reviews_rating_number']
                                        .mean()
                                        .nlargest(10)
                                        .sort_values(ascending=False)
                                        .to_frame()
                                        .reset_index())
        satisfaction_by_brand.columns = ['marca', 'media_avaliacoes']
        fig2 = px.bar(satisfaction_by_brand, x='marca', y='media_avaliacoes', text_auto='.2s')
        satisfaction_by_brand_table = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig2)
        col2.write(satisfaction_by_brand_table)

if __name__ == "__main__":
    Dashboard()
