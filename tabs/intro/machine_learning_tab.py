import streamlit as st
from tabs.tab import TabInterface

class IntroMachineLearningTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':blue[Machine Learning]', divider='blue')
            st.markdown('''                
                Durante o decorrer do projeto, foram utilizados modelos de machine learning em 2 momentos distintos, para abordar diferentes aspectos do problema em questão. Com isso, temos conforme à seguir:
                1) Na primeira abordagem, foi utilizado o algoritmo ensemble :blue[XGBoost], de forma a permitir que novos entrevistados sejam identificados como com COVID-19 ou não, sem a necessidade de realizar exames;
                2) Na segunda aboradgem, foi utilizado o algoritmo não supervisionado :blue[KMeans], com o intuíto de segmentar os entrevistados em diferentes grupos ou clusters;
                        
                A combinação desses modelos e técnicas proporcionará uma abordagem abrangente para analisar e extrair insights valiosos dos dados relacionados à COVID-19, incluindo previsões de casos confirmados e a segmentação dos entrevistados em grupos distintos, o que pode ser fundamental para orientar políticas de saúde pública e estratégias de combate à futuras pandemias.
            ''')

            st.markdown('''
            **:blue[Algoritmo ensemble: XGBoost]**\n\n
            Para a tarefa de prever se um novo entrevistado PNAD COVID-19 teria seu caso confirmado, foi escolhido o algoritmo :blue[XGBoost (Extreme Gradient Boosting)]. O :blue[XGBoost] é uma escolha comum em problemas de classificação, conhecido por sua eficácia em lidar com conjuntos de dados complexos e grandes, e por sua capacidade de lidar com sobreajuste. Este modelo será treinado com base em dados históricos, explorando padrões e relações nos dados para fazer previsões sobre a confirmação de casos.
            ''')

            st.markdown('''
            **:blue[Algoritmos não supervisionados: KMeans]**\n\n
            Já para a tarefa de agrupar os entrevistados em clusters com base em características semelhantes, foi decidido por explorar o algoritmo KMeans, disponível na biblioteca sklearn (scikit-learn) em Python. O :blue[KMeans] é um algoritmo de clusterização amplamente utilizado que agrupa os dados em k clusters.
            ''')

            st.markdown('''
            **:blue[Algoritmos não supervisionados no Google BigQuery: KMeans]**\n\n
            Ainda na questão de clusterização dos dados, foram realizados testes utilizando o algoritmo :blue[KMeans] diretamente no :blue[BigQuery]. A escolha de também utilizar tal abordagem, se deve à capacidade que o :blue[BigQuery] possui em lidar com grandes volumes de dados de forma eficiente e escalável, o que é crucial em projetos que lidam com conjuntos de dados extensos, como este relacionado à COVID-19 da PNAD 2020.\n
            Outro ponto interessante é que esta abordagem permite realizar uma comparação entre a aplicação do :blue[KMeans] de formas distintas.
            ''')