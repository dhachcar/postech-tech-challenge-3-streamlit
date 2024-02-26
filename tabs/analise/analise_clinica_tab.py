import streamlit as st
from tabs.tab import TabInterface

class AnaliseClinicaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Análise clínica]', divider='blue')
            st.markdown('''
                TESTE
            ''')

            st.image('assets/img/bigquery-evolucao-casos-mes-a-mes.png', caption='TODO: Melhorar esta legenda')
            st.image('assets/img/bigquery-evolucao-casos-mes-a-mes-por-uf.png', caption='TODO: Melhorar esta legenda')