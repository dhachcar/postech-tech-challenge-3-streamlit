import streamlit as st
from tabs.tab import TabInterface


class AnaliseProcessamentoMachineLearningUnsupervisedBigqueryTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Modelo KMeans BigQuery]", divider="blue"
            )
            st.markdown(
                """
                Utilizando os recursos poderosos do :blue[BigQuery], aplicamos o algoritmo KMeans para analisar os dados da PNAD COVID-19. Este modelo, embora construído com uma abordagem ligeiramente diferente em comparação com o modelo anteriormente desenvolvido via scikit-learn, ainda mantém o mesmo objetivo: segmentar os dados em grupos distintos para fornecer insights valiosos.\n
                É importante ressaltar que, apesar de algumas variações na metodologia de construção do modelo, o número de clusters ou centroides permaneceu consistente em :blue[5]. Essa escolha estratégica permite uma análise comparativa consistente entre os diferentes modelos e garante a coerência na interpretação dos resultados.\n
                Ao analisar os resultados deste modelo KMeans executado no :blue[BigQuery], esperamos identificar padrões interessantes nos dados da PNAD COVID-19, possibilitando uma compreensão mais profunda das diferentes características e comportamentos presentes na amostra entrevistada. Esses insights podem ser fundamentais para orientar políticas públicas, estratégias de saúde e outras decisões importantes relacionadas à futuras pandemias.
            """
            )

            st.image(
                "assets/img/bigquery-ml-1.png", caption="Criação do modelo KMeans dentro do BigQuery"
            )
            st.image(
                "assets/img/bigquery-ml-2.png", caption="Modelo KMeans no BigQuery"
            )
            st.image(
                "assets/img/bigquery-ml-3.png", caption="Executando o modelo e designando os registros para cada centroide"
            )

            st.subheader(
                ":blue[Sugestão de evolução futura]", divider="blue"
            )
            st.markdown(
                """
                Para desenvolvimentos futuros, a sugestão é integrar o :blue[BigQuery] à esta aplicação :blue[Streamlit] para consumirmos o modelo diretamente do :blue[BigQuery]. Vale notar que esta integração implicaria em gastos para o desenvolvimento do projeto, o que esta fora do escopo proposto.
            """
            )
