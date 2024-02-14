import streamlit as st
from tabs.tab import TabInterface

class IntroApacheSparkTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Apache Spark]', divider='blue')
            st.markdown('''
                O Apache Spark é um framework de computação distribuída de código aberto que oferece uma interface unificada para processamento de dados em larga escala, permitindo operações em memória para obter velocidades até 100 vezes mais rápidas que sistemas tradicionais. Com suporte para várias linguagens de programação e uma vasta gama de bibliotecas integradas, o Spark é amplamente utilizado para análise de big data em tempo real, processamento de dados em lotes, machine learning e muito mais, sendo uma escolha popular para empresas que buscam soluções eficientes e rápidas para lidar com grandes volumes de dados.\n\n
                Ele é o framework que será utilizado em conjunto com outras ferramentas (explicadas nas próximas seções) durante o desenvolvimento deste projeto.
            ''')