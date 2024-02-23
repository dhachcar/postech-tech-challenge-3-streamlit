import streamlit as st
from tabs.tab import TabInterface

class IntroArquiteturaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Arquitetura]', divider='blue')
            st.markdown('''
                Este projeto utiliza cinco ferramentas principais durante o seu andamento: **:blue[Apache Spark]**, **:blue[Google Colab]**, **:blue[Google Cloud Storage]**, **:blue[Google BigQuery]** e **:blue[Streamlit]**. 
                * O **:blue[Google Colab]** fornece um ambiente flexível e colaborativo baseado em nuvem para manipulação de dados com Python, análise exploratória e execução de algoritmos de machine learning, incluindo o uso do **:blue[Apache Spark]** para processamento distribuído. 
                * O **:blue[Google Cloud]** Storage é utilizado para armazenar os arquivos originais da PNAD COVID19, garantindo segurança e escalabilidade no armazenamento dos dados. 
                * O **:blue[Google BigQuery]** oferece uma solução de data warehouse totalmente gerenciada para armazenar e consultar grandes volumes de dados com rapidez e eficiência. 
                * Por fim, o **:blue[Streamlit]** é empregado na criação de um dashboard interativo para apresentação dos resultados do projeto, integrando-se de forma fluida com as demais ferramentas e proporcionando uma experiência de usuário intuitiva. 
            ''')

            st.image('assets/img/arquitetura.png', caption='Arquitetura do projeto')