import streamlit as st
from tabs.tab import TabInterface

class IntroGoogleBigQueryTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Google BigQuery]', divider='blue')
            st.markdown('''
                O Google BigQuery é um serviço de armazenamento e análise de dados na nuvem oferecido pelo Google. Ele permite que as organizações armazenem, consultem e analisem grandes volumes de dados de maneira rápida e eficiente, usando a linguagem de consulta SQL padrão. O BigQuery é altamente escalável, oferecendo capacidade de processamento sob demanda e integração fácil com outras ferramentas e serviços do ecossistema do Google Cloud Platform (GCP).\n\n
                O BigQuery é o serviço em nuvem escolhido para a realização deste trabalho.

                TODO: explicar oq é e como estou utilizando... colocar prints das tabelas criadas da PNAD\n\n
                gerar tabelas com as colunas (no bigquery, explicar que serão utilizadas 2 tipos de tabela, inicial e processado)
            ''')

            st.subheader(':blue[Tabelas]', divider='blue')
            st.markdown('''
                Dentro do BigQuery, temos 2 tipos de tabela:
                1) as tabelas com os dados originais;
                2) as tabelas processadas, contemplando exclusivamente as colunas/features que serão utilizadas durante o projeto;
                        
                As tabelas com os dados originais foram geradas a partir de arquivos CSV que foram enviados ao Google Cloud Storage, um serviço de armazenamento em nuvem (muito parecido com o S3 da Amazon).
            ''')