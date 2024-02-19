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
                O **:blue[Apache Spark]** é um framework de computação distribuída de código aberto que oferece uma interface unificada para processamento de dados em larga escala, permitindo operações em memória para obter velocidades até 100 vezes mais rápidas que sistemas tradicionais. Com suporte para várias linguagens de programação e uma vasta gama de bibliotecas integradas, o Spark é amplamente utilizado para análise de big data em tempo real, processamento de dados em lotes, machine learning e muito mais, sendo uma escolha popular para empresas que buscam soluções eficientes e rápidas para lidar com grandes volumes de dados.\n\n
                Ele é o framework que será utilizado em conjunto com outras ferramentas (explicadas nas próximas seções) durante o desenvolvimento deste projeto.\n\n
                Além disso, o **:blue[Spark]** será executado diretamente no **:blue[Google Colab]**, um ambiente de notebook baseado na nuvem, oferecendo uma maneira conveniente de explorar e analisar grandes conjuntos de dados. Alternativamente, poderíamos utilizar o **:blue[Dataproc]**, um serviço do Google Cloud Platform (GCP) projetado especificamente para processamento de dados em larga escala.\n\n
                O **:blue[Dataproc]** opera sob a infraestrutura do GCP, fornecendo um ambiente gerenciado e escalável para executar clusters do **:blue[Apache Spark]** e **:blue[Hadoop]**. No entanto, optamos por não utilizar o **:blue[Dataproc]** neste cenário específico devido à simplicidade e acessibilidade do **:blue[Google Colab]** para fins de demonstração ou análise exploratória, sem a necessidade de configurar e gerenciar um ambiente de cluster separado. Essa escolha permite uma configuração rápida e fácil para iniciar a análise de dados com o **:blue[Apache Spark]**, aproveitando a infraestrutura gratuita fornecida pelo **:blue[Google Colab]**.
            ''')