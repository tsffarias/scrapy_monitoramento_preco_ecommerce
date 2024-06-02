import pandas as pd
import sqlite3
import os
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

class Dashboard:

    def __init__(self):
        df = self.connect_db()
        self.layout(df)
        

    def layout(self, df):
        st.set_page_config(
            page_title="WebScraping",
            layout="wide",
            initial_sidebar_state="expanded")

        st.markdown("""
        <style>
        .big-font {
            font-size:80px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        #Options Menu
        with st.sidebar:
            selected = option_menu('WebScraping', ["Home", 'Mercado Livre', 'Magalu', 'Centauro', 'Netshoes', 'Sobre'], 
                icons=['house', 'search', 'search', 'search', 'search', 'info-circle'], menu_icon='intersect', default_index=0,
                styles={
                        "container": {"background-color": "#fafafa"},
                        "nav-link": {"--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#0068C9"},
                    }
                )
            
        # Menu Lateral
        if selected=="Home":
            self.home()
        elif selected=="Mercado Livre":
            self.mercado_livre(df)
        elif selected=="Amazon":
            self.amazon(df)
        elif selected=="Magalu":
            df = self.connect_db('magalu_items')
            self.magalu(df)
        elif selected=="Shopee":
            self.shopee(df)
        elif selected=="Centauro":
            df = self.connect_db('centauro_items')
            self.centauro(df)
        elif selected=="Netshoes":
            df = self.connect_db('netshoes_items')
            self.netshoes(df)
        else:
            self.about()
               
    
    def connect_db(self, table='mercadolivre_items'):
        relative_path_db_mercado_livre = '../../data/quotes.db'
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_db_mercado_livre))

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)

        # Carregar os dados da tabela em um DataFrame pandas
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

        # Fechar a conexão com o banco de dados
        conn.close()
        
        return df

    def home(self):
        #Header
        st.title('Monitoramento de Preços e Produtos E-commerce')
        st.subheader('*Pesquisa de Mercado - Tênis Esportivos 👟*')

        st.divider()

        with st.container():
            col1,col2=st.columns(2)
            with col1:
                st.header('Descrição')
                st.markdown(
                        """
                        Imagine que uma marca de tênis deseja avaliar sua relevância no ecossistema do Mercado Livre, Amazon, Magalu, Shopee e Centauro. 
                        Para isso, é necessário obter KPIs relacionados ao segmento de tênis nessas plataformas. 
                        O objetivo deste projeto é coletar informações detalhadas e implementar um dashboard que facilite a visualização e análise desses dados.
                    
                        ## Proposta do Projeto

                        Fomos contratados por uma grande empresa para fazer uma pesquisa de mercado na categoria de tênis esportivos dentro de diversos e-commerces: Mercado Livre, Amazon, Magalu, Shopee, Centauro. O objetivo dessa empresa é avaliar:
                        - 👟 Quais marcas são mais encontradas até a 10ª página
                        - 💰 Qual o preço médio por marca
                        - ⭐ Qual a satisfação por marca
                        """
                        )
            with col2:
                st.markdown(
                        """
                        ![Alt Text](https://www.scrapehero.com/wp/wp-content/uploads/2019/05/price-monitoring.gif)
                        """
                )

    def about(self):
        
        st.title('Data')
        
        col1,col2,col3=st.columns(3)
        col1.subheader('Fonte')
        col2.subheader('Descrição')
        col3.subheader('Link')
        with st.container():
            col1,col2,col3=st.columns(3)
            col1.write(':blue[Mercado Livre]')
            col2.write('Setor de Tênis corrida masculino')
            col3.write('https://lista.mercadolivre.com.br/tenis-corrida-masculino')
        
        with st.container():
            col1,col2,col3=st.columns(3)
            col1.write(':blue[Magalu]')
            col2.write('Setor de Tênis corrida masculino')
            col3.write('https://www.magazineluiza.com.br/busca/tenis%2Bmasculino/?from=clickSuggestion&filters=category---ES%2Bsubcategory---ELNN')

        with st.container():
            col1,col2,col3=st.columns(3)
            col1.write(':blue[Centauro]')
            col2.write('Setor de Tênis para academia masculino')
            col3.write('https://www.centauro.com.br/nav/produto/tenis/esportes/academiafitness/genero/masculino')
        
        with st.container():
            col1,col2,col3=st.columns(3)
            col1.write(':blue[Netshoes]')
            col2.write('Setor de Tênis corrida masculino')
            col3.write('https://www.netshoes.com.br/running/tenis-performance?genero=masculino')
        
        
        st.divider()
        
        st.title('Criador')
        with st.container():
            col1, col2= st.columns(2)
            col1.write('')
            col1.write('**Nome:** Thiago Silva Farias')
            col1.write('**Educação:**  Sistemas de Informações - UFMS')
            col1.write('**Experiencia:**  Analista de Dados e futuro Analytics Engineer')
            col1.write('**Contato:** [Linkedin](https://www.linkedin.com/in/thiagosilvafarias/)')
            col1.write('**Github:** [Projeto](https://github.com/tsffarias/scrapy_monitoramento_preco_ecommerce/tree/main)')
            col1.write('**Obrigado pela visita!**')

            col2.markdown(
                """
                ![Alt Text](https://www.scrapehero.com/wp/wp-content/uploads/2019/05/api-gif.gif)
                """
            )        

    def dashboard_elements(self, df):
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
        average_new_price = df['new_price_reais'].mean()
        col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

        st.divider()

        # Quais marcas são mais encontradas até a 10ª página
        st.subheader('👟 Marcas mais encontradas até a 10ª página')
        # Texto explicativo
        st.markdown(
            """
            **Descrição:** Este KPI avalia a visibilidade das marcas de tênis esportivos em e-commerces, contabilizando a frequência com que cada marca aparece até a 10ª página de resultados de pesquisa. 
            Essa métrica ajuda a identificar quais marcas têm maior presença e são mais facilmente encontradas pelos consumidores nas plataformas analisadas.
            """, 
            unsafe_allow_html=True
        )

        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = (df['brand']
                                    .value_counts()
                                    .nlargest(10)
                                    .sort_values(ascending=False)
                                    .to_frame()
                                    .reset_index())
        top_10_pages_brands.columns = ['marca', 'contagem']
        fig = px.bar(top_10_pages_brands, x='marca', y='contagem', text_auto='.3s')
        top_10_pages_brands_table = df['brand'].value_counts().sort_values(ascending=False)
        
        col1.plotly_chart(fig)
        col2.write(top_10_pages_brands_table)

        st.divider()

        # Qual o preço médio por marca
        st.subheader('💰 Preço médio por marca')
        st.markdown(
            """
            **Descrição:** Este KPI calcula o preço médio dos tênis esportivos de cada marca nas plataformas de e-commerce selecionadas. 
            Ele permite comparar o posicionamento de preço entre diferentes marcas e identificar quais marcas estão no segmento premium, médio ou de entrada, fornecendo insights valiosos sobre a estratégia de preços de cada marca.
            """, 
            unsafe_allow_html=True
        )
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = (df.groupby('brand')['new_price_reais']
                                        .mean()
                                        .nlargest(10)
                                        .sort_values(ascending=False)
                                        .to_frame()
                                        .reset_index())
        average_price_by_brand.columns = ['marca', 'preco_medio_novo']
        fig1 = px.bar(average_price_by_brand, x='marca', y='preco_medio_novo', text_auto='.3s')
        average_price_by_brand_table = df.groupby('brand')['new_price_reais'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig1)
        col2.write(average_price_by_brand_table)

        st.divider()

        # Qual a satisfação por marca
        st.subheader('⭐ Satisfação por marca')
        st.markdown(
            """
            **Descrição:** Este KPI mede a satisfação dos clientes com cada marca de tênis esportivos, utilizando as avaliações e classificações dos consumidores nas plataformas de e-commerce. 
            A média das avaliações por marca revela a percepção de qualidade e satisfação do cliente, destacando as marcas que têm melhor aceitação e aquelas que precisam de melhorias.
            """, 
            unsafe_allow_html=True
        )

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
        fig2 = px.bar(satisfaction_by_brand, x='marca', y='media_avaliacoes', text_auto='.3s')
        satisfaction_by_brand_table = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig2)
        col2.write(satisfaction_by_brand_table)
    
    def mercado_livre(self, df):
        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')
    
        # Imagem Logo e-commerce
        image_html = """
        <div style="text-align: center;">
            <img src="https://logopng.com.br/logos/mercado-livre-87.png" width="350" alt="Mercado Livre">
        </div>
        """

        # Renderiza o HTML na barra lateral
        st.sidebar.markdown(image_html, unsafe_allow_html=True)

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
        st.subheader('👟 Marcas mais encontradas até a 10ª página')
        st.markdown(
            """
            **Descrição:** Este KPI avalia a visibilidade das marcas de tênis esportivos em e-commerces, contabilizando a frequência com que cada marca aparece até a 10ª página de resultados de pesquisa. 
            Essa métrica ajuda a identificar quais marcas têm maior presença e são mais facilmente encontradas pelos consumidores nas plataformas analisadas.
            """, 
            unsafe_allow_html=True
        )
        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = (df['brand']
                                    .value_counts()
                                    .nlargest(10)
                                    .sort_values(ascending=False)
                                    .to_frame()
                                    .reset_index())
        top_10_pages_brands.columns = ['marca', 'contagem']
        fig = px.bar(top_10_pages_brands, x='marca', y='contagem', text_auto='.3s')
        top_10_pages_brands_table = df['brand'].value_counts().sort_values(ascending=False)
        
        col1.plotly_chart(fig)
        col2.write(top_10_pages_brands_table)

        st.divider()

        # Qual o preço médio por marca
        st.subheader('💰 Preço médio por marca')
        st.markdown(
            """
            **Descrição:** Este KPI calcula o preço médio dos tênis esportivos de cada marca nas plataformas de e-commerce selecionadas. 
            Ele permite comparar o posicionamento de preço entre diferentes marcas e identificar quais marcas estão no segmento premium, médio ou de entrada, fornecendo insights valiosos sobre a estratégia de preços de cada marca.
            """, 
            unsafe_allow_html=True
        )
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = (df.groupby('brand')['new_price']
                                        .mean()
                                        .nlargest(10)
                                        .sort_values(ascending=False)
                                        .to_frame()
                                        .reset_index())
        average_price_by_brand.columns = ['marca', 'preco_medio_novo']
        fig1 = px.bar(average_price_by_brand, x='marca', y='preco_medio_novo', text_auto='.3s')
        average_price_by_brand_table = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig1)
        col2.write(average_price_by_brand_table)

        st.divider()

        # Qual a satisfação por marca
        st.subheader('⭐ Satisfação por marca')
        st.markdown(
            """
            **Descrição:** Este KPI mede a satisfação dos clientes com cada marca de tênis esportivos, utilizando as avaliações e classificações dos consumidores nas plataformas de e-commerce. 
            A média das avaliações por marca revela a percepção de qualidade e satisfação do cliente, destacando as marcas que têm melhor aceitação e aquelas que precisam de melhorias.
            """, 
            unsafe_allow_html=True
        )
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
        fig2 = px.bar(satisfaction_by_brand, x='marca', y='media_avaliacoes', text_auto='.3s')
        satisfaction_by_brand_table = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)

        col1.plotly_chart(fig2)
        col2.write(satisfaction_by_brand_table)

    def magalu(self, df):
        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos na Magalu')  

        # Imagem Logo e-commerce
        image_html = """
        <div style="text-align: center;">
            <img src="https://images.tcdn.com.br/img/editor/up/691794/MagaluLogotipo1920x1080.png" width="350" alt="Magalu">
        </div>
        """ 
        # Renderiza o HTML na barra lateral
        st.sidebar.markdown(image_html, unsafe_allow_html=True) 

        self.dashboard_elements(df)  

    def centauro(self, df):
        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos na Centauro')

        # Imagem Logo e-commerce
        image_html = """
        <div style="text-align: center;">
            <img src="https://logodownload.org/wp-content/uploads/2017/08/centauro-logo-01.png" width="350" alt="Centauro">
        </div>
        """ 
        # Renderiza o HTML na barra lateral
        st.sidebar.markdown(image_html, unsafe_allow_html=True)

        self.dashboard_elements(df)

    def netshoes(self, df):
        # Título da aplicação
        st.title('Pesquisa de Mercado - Tênis Esportivos na Netshoes')

        # Imagem Logo e-commerce
        image_html = """
        <div style="text-align: center;">
            <img src="https://logodownload.org/wp-content/uploads/2020/02/netshoes-logo.png" width="350" alt="Netshoes">
        </div>
        """ 
        # Renderiza o HTML na barra lateral
        st.sidebar.markdown(image_html, unsafe_allow_html=True)

        self.dashboard_elements(df)

           

if __name__ == "__main__":
    Dashboard()
