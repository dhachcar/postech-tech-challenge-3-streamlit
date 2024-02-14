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
                TODO: explicar oq é e como estou utilizando... colocar prints das tabelas criadas da PNAD\n\n
                gerar tabelas com as colunas (no bigquery, explicar que serão utilizadas 2 tipos de tabela, inicial e processado)
            ''')