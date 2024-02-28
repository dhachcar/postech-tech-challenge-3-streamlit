import streamlit as st
from tabs.tab import TabInterface

class AnaliseProcessamentoMachineLearningEnsembleTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Machine Learning]', divider='blue')
            st.markdown('''
                TESTE - exportar/importar o modelo aqui (via joblib)
            ''')