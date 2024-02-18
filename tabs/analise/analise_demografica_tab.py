import streamlit as st
from tabs.tab import TabInterface

class AnaliseDemograficaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Análise demográfica]', divider='blue')
            st.markdown('''
                TESTE
            ''')